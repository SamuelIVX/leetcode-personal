export interface TopicTag {
  name: string;
}

export interface Problem {
  questionFrontendId: string;
  title: string;
  titleSlug: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  topicTags: TopicTag[];
}
