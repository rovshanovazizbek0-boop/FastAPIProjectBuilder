import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "path"

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    host: '0.0.0.0',
    port: 5000,
    // XATOLIKNI HAL QILUVCHI ASOSIY QISM:
    hmr: {
      clientPort: 443,
    },
    // Replit manziliga ruxsat berish
    allowedHosts: [
      '.replit.dev' 
    ],
    // API so'rovlari uchun proxy
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    }
  }
})