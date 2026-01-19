export interface Message {
  id: number
  role: 'user' | 'ai'
  content: string
}
