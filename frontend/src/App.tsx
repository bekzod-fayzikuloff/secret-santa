import React from 'react'
import './App.scss'
import MainLayout from './layouts/MainLayout'
import { Routes, Route } from 'react-router-dom'
import NotFoundPage from './pages/NotFoundPage'

function App() {
  return (
    <React.Fragment>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route path="*" element={<NotFoundPage />} />
        </Route>
      </Routes>
    </React.Fragment>
  )
}

export default App
