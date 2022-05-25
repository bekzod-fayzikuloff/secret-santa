import React from 'react'
import style from '../../assets/styles/Footer.module.scss'

export default function Footer() {
  return (
    <footer className={style.container}>
      <div className={style.footer_title}>
        <p>SecretSanta</p>
      </div>
      <div className={style.footer_description}>
        <p>Copyright ©2022 | Lorem ipsum dolor sit amet.</p>
      </div>
    </footer>
  )
}
