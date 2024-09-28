import Form from "../components/Form"

function Login() {
    return (
        <div className="flex justify-center items-center min-h-screen">
            <div className="p-8 rounded-lg shadow-md w-full max-w-sm">
                <Form route="/api/token/" method="login" />
            </div>
        </div>
    );
}

export default Login