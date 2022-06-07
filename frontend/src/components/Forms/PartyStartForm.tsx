import React, { SyntheticEvent, useState } from 'react'
import style from './../../assets/styles/HomePage.module.scss'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import Alert from './Alert'

interface FormEvent<T = Element> extends SyntheticEvent<T> {
  target: any
}

const PartyStartForm = () => {
  const [isFailedGameCreate, setFailedGameCreate] = useState(true)
  const navigate = useNavigate()

  const createParty = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const formData = {
      title: e.target.boxTitle.value,
      price_range: e.target.price.value,
      last_join_data: e.target.date.value,
      member_entry_message: e.target.message.value,
      manager: {
        first_name: e.target.managerFirstName.value,
        last_name: e.target.managerLastName.value,
        email: e.target.managerEmail.value
      }
    }
    axios
      .post(`${process.env.REACT_APP_API_PATH}boxes/`, formData)
      .then((reject) => {
        navigate(`u/${reject.data.manager.id}`)
      })
      .catch((reason) => {
        setFailedGameCreate(false)
      })
  }

  return (
    <div className={style.party__form}>
      <form onSubmit={createParty} action="">
        {isFailedGameCreate ? <></> : <Alert message={'All field should be filled'} />}
        <input type="date" name={'date'} placeholder={'Date of your Secret Santa party'} /> <br />
        <input type="number" name={'price'} placeholder={'Amount to spend'} /> <br />
        <input type="text" name={'boxTitle'} placeholder={'Secret Santa party title'} /> <br />
        <input
          type="text"
          name={'managerFirstName'}
          placeholder={'Secret Santa party Manager first name'}
        />{' '}
        <br />
        <input
          type="text"
          name={'managerLastName'}
          placeholder={'Secret Santa party Manager last name'}
        />{' '}
        <br />
        <input
          type="email"
          name={'managerEmail'}
          placeholder={'Secret Santa party Manager Email'}
        />{' '}
        <br />
        <input
          className={style.message__input}
          type="text"
          name={'message'}
          placeholder={'Add a personal message'}
        />{' '}
        <br />
        <button className={style.submit__button}>Submit</button>
      </form>
    </div>
  )
}

export default PartyStartForm
