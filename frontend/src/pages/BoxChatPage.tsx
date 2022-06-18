import React, {useEffect, useState} from "react";
import {useOutletContext} from "react-router-dom";
import {IUser} from "./BoxPage";
import axios from "axios";

export const BoxChatPage = () => {
  const user: IUser = useOutletContext()
  const [chatMessages, setChatMessages] = useState([])

    useEffect(() => {
    async function fetchData() {
      await axios
        .get(`${process.env.REACT_APP_API_PATH}boxes/${user?.box?.id}/chat/`)
        .then((res) => {
          setChatMessages(res.data)
        })
    }
    fetchData().then()
  }, [])

  return(
    <div>
      <p>{JSON.stringify(chatMessages)}</p>
    </div>
  )
}
