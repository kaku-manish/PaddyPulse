import { StrictMode, Suspense } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import './i18n' // Import i18n config
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Suspense fallback={<div className="flex h-screen items-center justify-center text-2xl font-bold">Loading Paddy Pulse...</div>}>
      <App />
    </Suspense>
  </StrictMode>,
)
