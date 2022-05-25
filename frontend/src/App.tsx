import React from 'react'
import './App.scss'
import MainLayout from './layouts/MainLayout'
import { Routes, Route } from 'react-router-dom'

function App() {
  return (
    <React.Fragment>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route path="/" element={<p>Main</p>} />
          <Route path="*" element={<p>404</p>} />
        </Route>
      </Routes>
    </React.Fragment>
  )
}

export default App
