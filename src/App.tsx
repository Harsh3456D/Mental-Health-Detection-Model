// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import "tailwindcss"

function App() {
  

  return (
    <>
    <header className="font-sans shadow-xl font-bold font-sm bg-black w-screen h-[8vh] m-auto py-8 px-10 fixed top-0 left-0">Mental health detection model</header>
    <img src='/ai2.png' className='w-[7vw] justify-self-center relative bottom-5'></img>
    <div className='font-sans shadow-xl bg-black w-[80vw] h-[60vh] overflow-auto rounded-2xl'>
    </div>
    <textarea className='font-sans resize-none [&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none] bg-black min-w-[75vw] h-[5vh] m-1 py-3 px-7 rounded-full fixed bottom-6 left-[10vw]' placeholder='Enter the text'></textarea>
    <button className='font-sans bg-black w-[4vw] h-[5vh] py-3 px-4 rounded-full fixed bottom-7 right-[10vw] transition ease-in-out hover:scale-105 hover:bg-blue-900'>Send</button>
    </>
  )
};

export default App
