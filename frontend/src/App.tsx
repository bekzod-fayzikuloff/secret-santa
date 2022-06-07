import React from 'react'
import './App.scss'
import MainLayout from './layouts/MainLayout'
import { Routes, Route, useNavigate } from 'react-router-dom'
import HomePage from './pages/HomePage'
import BoxPage from './pages/BoxPage'
import RulesPage from './pages/RulesPage'
import NotFoundPage from './pages/NotFoundPage'
import MainBoxPage from './components/Box/MainBoxPage'

function App() {
  const navigate = useNavigate()

  return (
    <React.Fragment>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/rules" element={<RulesPage />} />
          <Route path="u/:userUUID/" element={<BoxPage />}>
            <Route element={<MainBoxPage navigate={navigate} />}>
              <Route index element={<h1>Hello</h1>} />
              <Route path="game" element={<p>Game</p>} />
              <Route path="questionary" element={<p>Questionary</p>} />
              <Route path="chat" element={<p>Chat</p>} />
            </Route>
          </Route>
          <Route path="*" element={<NotFoundPage />} />
        </Route>
      </Routes>
    </React.Fragment>
  )
}

export default App
