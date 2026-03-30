import * as dotenv from 'dotenv';
dotenv.config();

import axios from 'axios';
import * as fs from 'fs';
import * as path from 'path';

import type { Problem } from './types';
import { LANG_EXT, DIFFICULTY_ICON, CATEGORY_ORDER, TAG_TO_CATEGORY } from './constants';

const LEETCODE_GRAPHQL = 'https://leetcode.com/graphql';
const USERNAME = process.env.LEETCODE_USERNAME ?? 'samuelhb';
const SESSION = process.env.LEETCODE_SESSION ?? '';
const SOLUTIONS_DIR = path.join(process.cwd(), 'solutions');

// --- Auth headers ---

function headers() {
  return {
    'Content-Type': 'application/json',
    Cookie: `LEETCODE_SESSION=${SESSION}`,
    Referer: 'https://leetcode.com',
  };
}

// --- GraphQL queries ---

async function fetchAllSolvedProblems(): Promise<Problem[]> {
  if (!SESSION) {
    throw new Error(
      'LEETCODE_SESSION is required.\n' +
      'Add it to your .env file: LEETCODE_SESSION=your_cookie_value'
    );
  }

  const query = `
    query solvedProblems($limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(
        categorySlug: ""
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        totalNum
        questions: data {
          questionFrontendId
          title
          titleSlug
          difficulty
          topicTags { name }
        }
      }
    }
  `;

  // Get total count first
  const first = await axios.post(
    LEETCODE_GRAPHQL,
    { query, variables: { limit: 1, skip: 0, filters: { status: 'AC' } } },
    { headers: headers() }
  );
  const total: number = first.data.data.problemsetQuestionList.totalNum;
  console.log(`Total solved on LeetCode: ${total}`);

  // Paginate in chunks of 100 (LeetCode's max per request)
  const PAGE_SIZE = 100;
  const problems: Problem[] = [];
  for (let skip = 0; skip < total; skip += PAGE_SIZE) {
    const res = await axios.post(
      LEETCODE_GRAPHQL,
      { query, variables: { limit: PAGE_SIZE, skip, filters: { status: 'AC' } } },
      { headers: headers() }
    );
    problems.push(...(res.data.data.problemsetQuestionList.questions as Problem[]));
  }
  return problems;
}

async function fetchLatestACSubmission(
  titleSlug: string
): Promise<{ id: string; lang: string } | null> {
  const query = `
    query latestACSubmission($questionSlug: String!) {
      questionSubmissionList(
        questionSlug: $questionSlug
        offset: 0
        limit: 1
        status: 10
      ) {
        submissions {
          id
          lang
        }
      }
    }
  `;
  try {
    const res = await axios.post(
      LEETCODE_GRAPHQL,
      { query, variables: { questionSlug: titleSlug } },
      { headers: headers() }
    );
    const subs = res.data.data.questionSubmissionList?.submissions ?? [];
    return subs.length > 0 ? subs[0] : null;
  } catch {
    return null;
  }
}

async function fetchSubmissionCode(submissionId: string): Promise<{ code: string; lang: string } | null> {
  const query = `
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang { name }
      }
    }
  `;
  try {
    const res = await axios.post(
      LEETCODE_GRAPHQL,
      { query, variables: { submissionId: parseInt(submissionId) } },
      { headers: headers() }
    );
    const details = res.data.data.submissionDetails;
    if (!details) return null;
    return { code: details.code, lang: details.lang.name };
  } catch {
    return null;
  }
}

// --- File helpers ---

function findExistingSolutionFile(titleSlug: string): string | null {
  const files = fs.readdirSync(SOLUTIONS_DIR);
  const match = files.find((f) => f.startsWith(`${titleSlug}.`));
  return match ? path.join(SOLUTIONS_DIR, match) : null;
}

function isStubFile(filePath: string): boolean {
  const content = fs.readFileSync(filePath, 'utf-8');
  return content.includes('// TODO: add your solution here');
}

function writeSolutionFile(problem: Problem, code: string, lang: string): void {
  const ext = LANG_EXT[lang] ?? lang;
  const tags = problem.topicTags.map((t) => t.name).join(', ');
  const commentChar = ['cpp', 'c', 'java', 'ts', 'js', 'go', 'swift', 'kt', 'rs', 'scala'].includes(ext)
    ? '//'
    : '#';

  const header = [
    ext === 'ts' || ext === 'js' ? '/**' : null,
    ` ${commentChar} Problem: ${problem.title}`,
    ` ${commentChar} Difficulty: ${problem.difficulty}`,
    ` ${commentChar} Link: https://leetcode.com/problems/${problem.titleSlug}/`,
    ` ${commentChar} Tags: ${tags || 'N/A'}`,
    ext === 'ts' || ext === 'js' ? ' */' : null,
  ]
    .filter(Boolean)
    .join('\n');

  const filePath = path.join(SOLUTIONS_DIR, `${problem.titleSlug}.${ext}`);
  fs.writeFileSync(filePath, `${header}\n\n${code}\n`, 'utf-8');
}

function writeStub(problem: Problem): void {
  const tags = problem.topicTags.map((t) => t.name).join(', ');
  const stub = `/**
 * Problem: ${problem.title}
 * Difficulty: ${problem.difficulty}
 * Link: https://leetcode.com/problems/${problem.titleSlug}/
 * Tags: ${tags || 'N/A'}
 */

function solution() {
  // TODO: add your solution here
}
`;
  fs.writeFileSync(path.join(SOLUTIONS_DIR, `${problem.titleSlug}.ts`), stub, 'utf-8');
}

// --- README generation ---

function categorize(problem: Problem): string {
  for (const tag of problem.topicTags) {
    const category = TAG_TO_CATEGORY[tag.name];
    if (category) return category;
  }
  return 'Other';
}

function problemRow(p: Problem): string {
  const icon = DIFFICULTY_ICON[p.difficulty] ?? '';
  const tags = p.topicTags.map((t) => t.name).join(', ');
  const existing = findExistingSolutionFile(p.titleSlug);
  const hasRealSolution = existing && !isStubFile(existing);
  const solution = hasRealSolution
    ? `[Solution](${path.relative(process.cwd(), existing!)})`
    : '—';
  return `| ${p.questionFrontendId} | [${p.title}](https://leetcode.com/problems/${p.titleSlug}/) | ${icon} ${p.difficulty} | ${tags || '—'} | ${solution} |`;
}

function generateReadme(problems: Problem[]): string {
  const easy = problems.filter((p) => p.difficulty === 'Easy').length;
  const medium = problems.filter((p) => p.difficulty === 'Medium').length;
  const hard = problems.filter((p) => p.difficulty === 'Hard').length;
  const today = new Date().toISOString().split('T')[0];

  // Group problems by category
  const groups = new Map<string, Problem[]>();
  for (const p of problems) {
    const cat = categorize(p);
    if (!groups.has(cat)) groups.set(cat, []);
    groups.get(cat)!.push(p);
  }

  const DIFF_ORDER: Record<string, number> = { Easy: 0, Medium: 1, Hard: 2 };

  // Sort problems within each category by difficulty, then by problem number
  for (const [, list] of groups) {
    list.sort(
      (a, b) =>
        (DIFF_ORDER[a.difficulty] ?? 0) - (DIFF_ORDER[b.difficulty] ?? 0) ||
        parseInt(a.questionFrontendId) - parseInt(b.questionFrontendId)
    );
  }

  const TABLE_HEADER = `| # | Problem | Difficulty | Tags | Solution |\n|---|---------|------------|------|----------|`;

  const sections = CATEGORY_ORDER
    .filter((cat) => groups.has(cat))
    .map((cat) => {
      const rows = groups.get(cat)!.map(problemRow).join('\n');
      return `### ${cat}\n\n${TABLE_HEADER}\n${rows}`;
    })
    .join('\n\n');

  return `# LeetCode Solutions

> Auto-synced from LeetCode. Solutions are primarily written in Python.

## Stats

| Total | 🟢 Easy | 🟡 Medium | 🔴 Hard |
|-------|---------|----------|---------|
| **${problems.length}** | ${easy} | ${medium} | ${hard} |

## Problems

${sections}

---

*Last synced: ${today}*
`;
}

// --- Main ---

async function main(): Promise<void> {
  if (!fs.existsSync(SOLUTIONS_DIR)) {
    fs.mkdirSync(SOLUTIONS_DIR);
  }

  console.log(`Fetching all solved problems for "${USERNAME}"...`);
  const problems = await fetchAllSolvedProblems();
  console.log(`Fetched ${problems.length} solved problems\n`);

  let fetched = 0;
  let skipped = 0;
  let stubbed = 0;

  for (const problem of problems) {
    const existing = findExistingSolutionFile(problem.titleSlug);

    // Skip if a real (non-stub) solution file already exists
    if (existing && !isStubFile(existing)) {
      skipped++;
      continue;
    }

    process.stdout.write(`  [${problem.questionFrontendId}] ${problem.title}... `);

    const submission = await fetchLatestACSubmission(problem.titleSlug);
    await new Promise((r) => setTimeout(r, 300));

    if (!submission) {
      writeStub(problem);
      process.stdout.write('stub (no submission found)\n');
      stubbed++;
      continue;
    }

    const result = await fetchSubmissionCode(submission.id);
    await new Promise((r) => setTimeout(r, 300));

    if (!result) {
      writeStub(problem);
      process.stdout.write('stub (could not fetch code)\n');
      stubbed++;
      continue;
    }

    writeSolutionFile(problem, result.code, result.lang);
    process.stdout.write(`saved (${result.lang})\n`);
    fetched++;
  }

  console.log(`\nResults: ${fetched} fetched, ${stubbed} stubbed, ${skipped} already had solutions`);

  console.log('\nGenerating README.md...');
  fs.writeFileSync(path.join(process.cwd(), 'README.md'), generateReadme(problems), 'utf-8');
  console.log(`Done. ${problems.length} problems synced.`);
}

main().catch((err) => {
  console.error(err.message ?? err);
  process.exit(1);
});
