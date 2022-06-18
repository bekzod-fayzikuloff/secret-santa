import React, {useEffect, useState} from "react";
import {FormEvent} from "../components/Forms/PartyStartForm";
import {IUser} from "./BoxPage";
import {useOutletContext} from "react-router-dom";
import axios from "axios";
import style from "../assets/styles/Questionary.module.scss"


interface Questionary {
  id?: string
  content?: string
}

const BoxQuestionaryPage = () => {
  const user: IUser = useOutletContext()
  const [questionary, setQuestionary] = useState<Questionary>({})

  // useEffect(() => {
  //   document.title = "Questionary"
  // }, [])

  useEffect(() => {
    (async () => {
      await axios
        .get(`${process.env.REACT_APP_API_PATH}users/${user.id}/questionary/`)
        .then((res) => {
          setQuestionary({
            id: res.data.id,
            content: res.data.content
          })
        }).catch((reason) => {
          if (reason.request.status === 404) {
            return
          }
        })
    })()
  }, [user])

  const handleQuestionarySubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    (async () => {
      await axios
        .patch(
          `${process.env.REACT_APP_API_PATH}boxes/${user.box?.id}/questionnaires/${questionary?.id}/`,
          {content: e.target.questionary.value}
        )
        .then((res) => {
          setQuestionary({
            id: res.data.id,
            content: res.data.content
          })
        }).catch((reason) => {
          (async () => {
            await axios
              .post(
                `${process.env.REACT_APP_API_PATH}boxes/${user?.box?.id}/questionnaires/`,
                {
                  content: e.target.questionary.value,
                    maker: {
                      first_name: user.first_name,
                      last_name: user.last_name,
                      email: user.email
                  }
                }
              )
          })()
        });
    })()
  }

  return(
    <main className={style.root}>

      <div className={style.form__wrapper}>
        <form className={style.questionary__form} onSubmit={handleQuestionarySubmit}>
          <input type="text" name={"questionary"}/> <br/>
          <input type="submit"/>
        </form>
      </div>

      <div className={style.questionary__text_container}>
        <p className={style.questionary__text}>{questionary.content}</p>
      </div>
    </main>
  )
}


export default BoxQuestionaryPage;
