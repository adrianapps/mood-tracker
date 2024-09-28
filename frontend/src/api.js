import axios from "axios"
import { ACCESS_TOKEN } from "./constants"
import { jwtDecode } from "jwt-decode"

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

const getUserIdFromToken = () => {
    const token = localStorage.getItem(ACCESS_TOKEN)
    if (token) {
        const decodedToken = jwtDecode(token)
        return decodedToken.user_id
    }
    return null;
};

export default api;
export { getUserIdFromToken };