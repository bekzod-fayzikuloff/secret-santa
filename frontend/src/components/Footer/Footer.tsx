import React from 'react'
import style from '../../assets/styles/Footer.module.scss'
import { useNavigate } from 'react-router-dom'

export default function Footer() {
  const navigate = useNavigate()
  return (
    <footer className={style.container}>
      <div className={style.footer_title} onClick={() => navigate('/')}>
        <p>SecretSanta</p>
      </div>
      <div className={style.footer_description}>
        <p>Copyright ©2022 | Lorem ipsum dolor sit amet.</p>
      </div>
    </footer>
  )
}
