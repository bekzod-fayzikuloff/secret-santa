import React from 'react'
import style from '../assets/styles/HomePage.module.scss'

export default function RulesPage() {
  return (
    <main className={style.root}>
      <div className={style.container}>
        <h3>What Is Secret Santa? Rules for How to Play a Secret Santa Gift Exchange Online</h3>
        <p>
          You might know it as a Yankee Swap or a White Elephant, but around the world, from office
          conference rooms to holiday house parties, gift exchange games have become a
          not-to-be-missed tradition amongst friends, families, and coworkers. But there’s really
          only one king of the Christmas gift exchange: Secret Santa. It’s the game that keeps alive
          the mystery, suspense, and surprise of holiday gifting, turning average joes into sneaky
          elves.
        </p>{' '}
        <br />
        <h3>So what is Secret Santa, you ask?</h3> <br />
        <p>
          Secret Santa is a Christmas tradition. Members of a group of friends, family, or coworkers
          draw random names to become someone’s Secret Santa. The Secret Santa is given a wish list
          of gift ideas to choose from to give to their chosen giftee. After opening their present,
          the giftee has to guess which member of the group was their Secret Santa. It’s a holiday
          classic where the guessing is as much a part of the fun as receiving the gift.
        </p>{' '}
        <br />
        <p>
          While everyone seems to have some of their own rules when it comes to Secret Santa, the
          idea can be traced back to the Scandinavian tradition of knocking on someone’s door,
          throwing a present inside when it opens, then running away. They call this Juklapp, or
          “knocking Christmas.” Or, roots may trace back even further to German legends about St.
          Nick’s helpers, who doled out presents to good kids, but not to the bad, but one thing is
          for certain. The tradition continues to evolve over the years.
        </p>{' '}
        <br />
        <p>
          Online Secret Santa games now offer a modern twist on a classic, letting anyone elf it up
          from anywhere around the world. It’s an update on a beloved game that expands the idea of
          who a Secret Santa can be: your little elf can be anyone from your neighbor down the
          street to a remote coworker on the other side of the world. But whether you’re playing a
          traditional Secret Santa exchange or an online one, there are rules to ensure mystery,
          merriment, and a little elvish magic.
        </p>{' '}
        <br />
        <h3>How to Play Secret Santa: Traditional Game Rules</h3> <br />
        <p>
          Traditional Secret Santa rules, in essence, are pretty simple: no one knows who is getting
          whom a gift. But organizing a gift exchange with your friends, family, or coworkers can be
          a bit more complicated. Here are the steps for hosting a traditional Secret Santa game
          in-person:
        </p>
        <ol className={style.rules__list}>
          <li>
            Write down each name on a piece of paper. Gather all the participants up and have them
            scribble their names on a piece of paper. Encourage legibility, otherwise you’ll have
            people buying gifts for “does that say...Floger? Smoged?” If it’s hard to get them all
            in the same room, you can do this yourself after each person agrees by text or email to
            go full elf.
          </li>
          <li>
            Have everyone write down a gift suggestion or two. Players can write down something
            specific like thick red knee high socks, or something pretty vague like “a book,
            please.” The more specific the better, though, to ensure everyone gets something they
            actually want.
          </li>
          <li>
            Draw names to randomly assign a Secret Santa to each player. This is the fun part; reach
            into the hat and find out whose Christmas you’ll be making better! The host can also do
            this solo and email, call, or text the other players their assigned name—just make sure
            you keep things straight with a top secret list of who’s assigned to whom. Not even
            Rudolph can help you if you lose the master list!
          </li>
          <li>
            Plan a gift exchange party. Pick a day when everyone can get together, preferably before
            people leave for their Christmas vacations. Make sure each gift is tagged with the
            recipient’s name, but not the gifter’s! Exchange gifts, goodies, and holiday cheer to
            last all year.
          </li>
          <li>
            Guess who drew your name. Guessing who your sneaky Secret Santa is, and revealing your
            own elfy nature to the person you gifted a present to, is the reindeer’s knees. Who got
            you the book for your next book club meeting? Who knows how much you’ve been craving
            chocolate? Was it Allison? No? Then it must be...Allison? Wait, did I already guess
            that?
          </li>
        </ol>{' '}
        <br />
        <p>
          All that is fun of course. But what if you want an easier way to handle a big group, to
          make sure Sally doesn’t get picked twice while Steve gets left out in the snow? Or maybe
          you want to be able to expand your group from the North to the South Pole. No reason to
          doubt the magic of the elves! Santa’s gone digital with an online version of the gifting
          favorite.
        </p>{' '}
        <br />
        <h3>How to Play Secret Santa Online: The Modern, Updated Rules</h3> <br />
        <p>
          Say you want to set up a Secret Santa game for friends around the country—or even the
          world. Maybe it’s to bring together all of your distant relatives, or the Game of Thrones
          forum group you run. Any community of people, from anywhere on the planet, can join
          together for a Secret Santa extravaganza. Here are the rules for getting your online gift
          exchange started:
        </p>
        <ol className={style.rules__list}>
          <li>
            Invite the other elves, er, players. Set up an online Secret Santa gift exchange, then
            email an invitation to everyone in your group who might want to get their elf on.
          </li>
          <li>
            Randomize the name selection. Digital Secret Santa name generation tools randomly send
            out assignments and wish lists, keeping track of a master list of paired up participants
            for the host, no pom-pom’ed hat required.
          </li>
          <li>
            Create comprehensive wish lists. Participants can create a wish list using gifts or
            gifting inspirations from any major outlet, including Amazon, Etsy, Target, and more!
            Just set a spending limit and let them wish to their hearts’ content. You can also send
            out a Secret Santa Questionnaire so you don’t accidentally blow your cover by trying to
            subtly ask what size sock someone wears (just out of curiosity, no reason, you know).
          </li>
          <li>
            Exchange gifts. Wrap your gifts and send them on. Or, make it even easier by selecting
            items from their wish list and have the gifts shipped directly, so all you have to do is
            set a delivery date.
          </li>
          <li>
            Host a global party. Set up a video chat party to open your gifts and reveal your elfish
            identities; geography is no longer a limitation.
          </li>
          <li>
            Guess who drew your name. Well, you can’t update a classic. The guessing can be the
            same, or, if you want, names can be written on the cards that get delivered with the
            gifts. But come on, it still isn’t Allison.
          </li>
        </ol>
        <br />
      </div>
    </main>
  )
}
