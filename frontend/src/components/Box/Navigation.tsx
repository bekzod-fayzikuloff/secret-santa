import React from 'react'
import { Navigation } from 'react-minimal-side-navigation'
import { MdDashboard } from 'react-icons/md'
import { TiMail } from 'react-icons/ti'
import { RiChat3Line } from 'react-icons/ri'

export default function Navigate(props: { onSelect: CallableFunction }) {
  return (
    <>
      <Navigation
        activeItemId="/dashboard"
        onSelect={({ itemId }) => props.onSelect(itemId)}
        items={[
          {
            title: 'Dashboard',
            itemId: '/game',
            // you can use your own custom Icon component as well
            // icon is optional
            elemBefore: () => <MdDashboard />
          },
          {
            title: 'Questionary',
            itemId: '/questionary',
            elemBefore: () => <TiMail />
          },
          {
            title: 'Chat',
            itemId: '/chat',
            elemBefore: () => <RiChat3Line />
          },
          {
            title: 'Rules',
            itemId: '/rules'
          }
        ]}
      />
    </>
  )
}
