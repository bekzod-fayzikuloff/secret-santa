import React from 'react'
import style from './../../assets/styles/Form.module.scss'

const Alert = (props: { message: string }) => {
  const { message } = props
  return (
    <div className={style.alert}>
      <p>{message}</p>
    </div>
  )
}

export default Alert
