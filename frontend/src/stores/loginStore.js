import { create } from "zustand";

const useLogin = create((set) => ({
  loggedIn: true ? localStorage.getItem("access_token") != null : false,
  setLoginState: (newState) => set({ loggedIn: newState }),
}));

export default useLogin;