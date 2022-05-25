import React from 'react'
import SnowStorm from 'react-snowstorm'
import style from '../../assets/styles/Header.module.scss'
import HeaderIcon from './HeaderIcon'

function Header() {
  return (
    <header id="header" className={style.container}>
      <SnowStorm targetElement="header" snowStick={false} />
      <HeaderIcon />
    </header>
  )
}

export default Header
