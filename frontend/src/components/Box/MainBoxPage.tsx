import React from 'react'
import style from '../../assets/styles/MainBoxPage.module.scss'
import 'react-minimal-side-navigation/lib/ReactMinimalSideNavigation.css'
import {NavigateFunction, Outlet, useOutletContext, useParams} from 'react-router-dom'
import Navigate from './Navigation'
import { UserUUID } from '../../pages/BoxPage'

const MainBoxPage = (props: { navigate: NavigateFunction }) => {
  const { navigate } = props
  const { userUUID }: UserUUID = useParams()
  const context = useOutletContext()

  const onSelect = (path: string): void => {
    if (path === '/rules') {
      navigate(`${path}`)
    } else {
      navigate(`u/${userUUID}${path}`)
    }
  }
  return (
    <div className={style.root}>
      <div className={style.navigation}>
        <Navigate onSelect={onSelect} />
      </div>
      <div className={style.content}>
        <Outlet context={context}/>
      </div>
    </div>
  )
}

export default MainBoxPage
