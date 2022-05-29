import React from 'react'
import './App.scss'
import MainLayout from './layouts/MainLayout'
import { Routes, Route } from 'react-router-dom'
import HomePage from './pages/HomePage'
import BoxPage from './pages/BoxPage'
import RulesPage from './pages/RulesPage'
import NotFoundPage from './pages/NotFoundPage'

function App() {
  return (
    <React.Fragment>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/rules" element={<RulesPage />} />
          <Route path="u/:userUUID" element={<BoxPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Route>
      </Routes>
    </React.Fragment>
  )
}

export default App
