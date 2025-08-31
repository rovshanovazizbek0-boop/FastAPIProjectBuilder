import { Routes, Route, Navigate } from "react-router-dom";
import { LoginPage } from "./pages/Login";

// Vaqtinchalik Dashboard sahifasi
function DashboardPage() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold">Asosiy Sahifa (Dashboard)</h1>
      <p>Siz tizimga muvaffaqiyatli kirdingiz!</p>
    </div>
  );
}

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route path="/dashboard" element={<DashboardPage />} />
      <Route path="*" element={<Navigate to="/login" />} />
    </Routes>
  );
}

export default App;