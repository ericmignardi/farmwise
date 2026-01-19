<script setup lang="ts">
import { axiosInstance } from '@/services/api'
import { ArrowUp } from 'lucide-vue-next'
import { ref } from 'vue'
import { marked } from 'marked'
import type { Message } from '@/types/chat/types'

const message = ref<string>('')
const messages = ref<Message[]>([])
const loading = ref<boolean>(false)

const chatContainer = ref()

const renderMessage = (content: string) => {
  return marked.parse(content)
}

const sendMessage = async () => {
  if (!message.value) return

  loading.value = true
  const currentMessage = message.value

  messages.value.push({
    id: Date.now(),
    role: 'user',
    content: currentMessage,
  })

  message.value = ''

  try {
    const response = await axiosInstance.post('/chat/', {
      message: currentMessage,
    })

    if (response.status === 200) {
      messages.value.push({
        id: Date.now() + 1,
        role: 'ai',
        content: response.data.response,
      })
    }
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <main class="overflow-y-auto flex flex-col gap-4 p-4">
    <!-- Chat Container -->
    <div ref="chatContainer" class="p-4 flex flex-col gap-4">
      <div
        v-for="msg in messages"
        :key="msg.id"
        class="flex"
        :class="msg.role === 'user' ? 'justify-end' : 'justify-start'"
      >
        <div
          class="rounded-lg p-3 max-w-[80%]"
          :class="msg.role === 'user' ? 'bg-green-500 text-stone-950' : 'bg-gray-100 text-gray-800'"
          v-html="renderMessage(msg.content)"
        ></div>
      </div>
      <div v-if="loading" class="bg-gray-100 text-gray-800 text-sm italic">Thinking...</div>
    </div>
    <!-- Chat Input -->
    <div>
      <input
        name="message"
        v-model="message"
        @keyup.enter="sendMessage"
        placeholder="Ask anything"
      />
      <button @click="sendMessage"><ArrowUp /></button>
    </div>
  </main>
</template>

<style scoped>
:deep(ul) {
  list-style-type: disc;
  padding-left: 1.5rem;
}
:deep(ol) {
  list-style-type: decimal;
  padding-left: 1.5rem;
}
:deep(li) {
  margin-bottom: 0.25rem;
}
:deep(p) {
  margin-bottom: 0.75rem;
}
:deep(h1),
:deep(h2),
:deep(h3) {
  font-weight: 600;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}
</style>
