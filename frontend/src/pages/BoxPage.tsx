import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios, { AxiosError } from 'axios'
import NotFoundPage from './NotFoundPage'
import MainBoxPage from '../components/Box/MainBoxPage'

/*
 * TypeScript types and interfaces define
 */
type UserUUID = {
  userUUID?: string
}

interface Box {
  id?: string
  price_range?: number
  title?: string
  manager?: any
}

export interface IUser {
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
  const [user, setUser] = useState<IUser>({})
  const [isExistUser, setExistUser] = useState(true)

  useEffect(() => {
    async function fetchData() {
      const userData = await axios
        .get(`${process.env.REACT_APP_API_PATH}users/${userUUID}`)
        .then((res) => {
          console.log(res.data)
          return res.data
        })
        .catch((reason: AxiosError) => {
          if (reason.response?.status === 404) {
            setExistUser(false)
          }
        })
      setUser(userData)
    }
    fetchData().then()
  }, [])

  return (
    <React.Fragment>{isExistUser ? <MainBoxPage user={user} /> : <NotFoundPage />}</React.Fragment>
  )
}
