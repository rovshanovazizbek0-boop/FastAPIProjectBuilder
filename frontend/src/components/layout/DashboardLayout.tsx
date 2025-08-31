import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";

export function DashboardLayout({ children }: { children: React.ReactNode }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    navigate("/login");
  };

  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-background border-b shadow-sm">
        <div className="container mx-auto h-16 flex items-center justify-between">
          <h1 className="text-xl font-bold">BotFactory</h1>
          <Button variant="outline" onClick={handleLogout}>
            Chiqish
          </Button>
        </div>
      </header>
      <main className="flex-1 container mx-auto py-8">
        {children}
      </main>
    </div>
  );
}