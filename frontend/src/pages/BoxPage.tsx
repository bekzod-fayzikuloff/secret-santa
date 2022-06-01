import React, { useEffect, useState } from 'react'
import { useParams, Outlet } from 'react-router-dom'
import axios, { AxiosError } from 'axios'
import NotFoundPage from './NotFoundPage'
// import MainBoxPage from '../components/Box/MainBoxPage'

/*
 * TypeScript types and interfaces define
 */
export type UserUUID = {
  userUUID?: string
}

export interface Box {
  id?: string
  price_range?: number
  title?: string
  manager?: any
}

export interface IUser {
  id?: string
  email?: string
  first_name?: string
  last_name?: string
  box?: Box
}

/*
################################
*/

export default function BoxPage() {
  const { userUUID }: UserUUID = useParams()
  const [isExistUser, setExistUser] = useState(true)

  useEffect(() => {
    async function fetchData() {
      await axios
        .get(`${process.env.REACT_APP_API_PATH}users/${userUUID}`)
        .then((res) => {})
        .catch((reason: AxiosError) => {
          if (reason.response?.status === 404) {
            setExistUser(false)
          }
        })
    }
    fetchData().then()
  }, [])

  return <React.Fragment>{isExistUser ? <Outlet /> : <NotFoundPage />}</React.Fragment>
}
