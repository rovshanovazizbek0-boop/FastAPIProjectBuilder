// frontend/src/pages/Dashboard.tsx faylining yangi tarkibi
import { useEffect, useState, useCallback } from "react";
import { DashboardLayout } from "@/components/layout/DashboardLayout";
import apiClient from "@/lib/api";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import { CreateBotDialog } from "@/components/CreateBotDialog";

interface Bot {
  id: number;
  telegram_token: string;
  status: 'TRIAL' | 'ACTIVE' | 'INACTIVE';
  plan_type: 'TRIAL' | 'MONTHLY' | 'YEARLY';
  default_language: string;
}

export function DashboardPage() {
  const [bots, setBots] = useState<Bot[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const fetchBots = useCallback(async () => {
    setLoading(true);
    try {
      const response = await apiClient.get('/bots/me');
      setBots(response.data);
    } catch (err) {
      setError("Botlarni yuklashda xatolik yuz berdi.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchBots();
  }, [fetchBots]);

  const maskToken = (token: string) => token.substring(0, 12) + '...';

  return (
    <DashboardLayout>
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-semibold">Mening Botlarim</h2>
        <CreateBotDialog onBotCreated={fetchBots} />
      </div>

      {loading && <p>Yuklanmoqda...</p>}
      {error && <p className="text-red-500">{error}</p>}

      {!loading && !error && (
        <div className="border rounded-lg">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>ID</TableHead>
                <TableHead>Telegram Token</TableHead>
                <TableHead>Status</TableHead>
                <TableHead>Til</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {bots.length > 0 ? (
                bots.map((bot) => (
                  <TableRow key={bot.id}>
                    <TableCell className="font-medium">{bot.id}</TableCell>
                    <TableCell>{maskToken(bot.telegram_token)}</TableCell>
                    <TableCell>
                      <Badge variant={bot.status === 'ACTIVE' ? 'default' : 'secondary'}>{bot.status}</Badge>
                    </TableCell>
                    <TableCell>{bot.default_language.toUpperCase()}</TableCell>
                  </TableRow>
                ))
              ) : (
                <TableRow>
                  <TableCell colSpan={4} className="text-center">Hali botlaringiz yo'q. Birinchisini qo'shing!</TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </div>
      )}
    </DashboardLayout>
  );
}