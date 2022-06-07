import React from 'react'
import style from './../assets/styles/HomePage.module.scss'
import PartyStartForm from '../components/Forms/PartyStartForm'

export default function HomePage() {
  return (
    <main className={style.root}>
      <div className={style.container}>
        <h2>What is Secret Santa?</h2>
        <p>
          It’s a free online Secret Santa gift exchange organizer / Kris Kringle generator! Organize
          a Secret Santa party with friends, family or even co-workers. After receiving the Secret
          Santa mail you can add your own wishlist, which will be delivered to your Secret Santa
        </p>
        <p>
          Each year around Christmas time people all over the world exchange gifts. To keep things
          interesting though, you can randomly assign persons to each other to give a present to one
          another.
        </p>
        <h3>How does it work?</h3>
        <p>Create a party on the homepage</p>

        <PartyStartForm />
      </div>
    </main>
  )
}
