import { create } from "zustand";

const useUserId = create((set) => ({
  useId: "",
  setUserId: (newUserId) => set({ useId: newUserId }),
}));

export default useUserId;
