import { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="min-h-screen bg-background text-foreground">
      <div className="container mx-auto px-4 py-8">
        <div className="text-center">
          <h1 className="text-4xl font-bold mb-8 text-primary">
            Frontend loyihasi qayta qurildi!
          </h1>
          
          <div className="bg-card p-6 rounded-lg border shadow-sm max-w-md mx-auto">
            <h2 className="text-2xl font-semibold mb-4 text-card-foreground">
              Tailwind CSS Test
            </h2>
            
            <button 
              onClick={() => setCount((count) => count + 1)}
              className="bg-primary text-primary-foreground hover:bg-primary/90 px-4 py-2 rounded-md transition-colors"
            >
              Count: {count}
            </button>
            
            <p className="mt-4 text-muted-foreground">
              Agar bu tugma chiroyli ko'rinishda bo'lsa, Tailwind CSS to'g'ri ishlayapti!
            </p>
          </div>

          <div className="mt-8 space-y-2">
            <p className="text-green-600 font-medium">✅ Vite + React TypeScript</p>
            <p className="text-blue-600 font-medium">✅ Tailwind CSS + shadcn/ui tema</p>
            <p className="text-purple-600 font-medium">✅ PostCSS konfiguratsiyasi</p>
            <p className="text-orange-600 font-medium">✅ Replit proxy sozlamalari</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
