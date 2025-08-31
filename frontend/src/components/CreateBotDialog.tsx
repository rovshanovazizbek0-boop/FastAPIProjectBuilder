// frontend/src/components/CreateBotDialog.tsx fayli
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import apiClient from "@/lib/api";

export function CreateBotDialog({ onBotCreated }: { onBotCreated: () => void }) {
  const [open, setOpen] = useState(false);
  const [token, setToken] = useState("");
  const [kbUz, setKbUz] = useState("");
  const [kbRu, setKbRu] = useState("");
  const [kbEn, setKbEn] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      await apiClient.post("/bots/", {
        telegram_token: token,
        knowledge_base_uz: kbUz,
        knowledge_base_ru: kbRu,
        knowledge_base_en: kbEn,
      });
      setOpen(false); // Oynani yopish
      onBotCreated(); // Ro'yxatni yangilash uchun
    } catch (err) {
      setError("Bot yaratishda xatolik yuz berdi.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button>Yangi bot qo'shish</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[625px]">
        <DialogHeader>
          <DialogTitle>Yangi Bot Yaratish</DialogTitle>
          <DialogDescription>Bot ma'lumotlarini kiriting. Bilimlar bazasini keyinroq ham to'ldirishingiz mumkin.</DialogDescription>
        </DialogHeader>
        <form onSubmit={handleSubmit}>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="token" className="text-right">Telegram Token</Label>
              <Input id="token" value={token} onChange={(e) => setToken(e.target.value)} className="col-span-3" required />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="kb_uz" className="text-right">Bilimlar bazasi (UZ)</Label>
              <Textarea id="kb_uz" value={kbUz} onChange={(e) => setKbUz(e.target.value)} className="col-span-3" rows={4} />
            </div>
             <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="kb_ru" className="text-right">Bilimlar bazasi (RU)</Label>
              <Textarea id="kb_ru" value={kbRu} onChange={(e) => setKbRu(e.target.value)} className="col-span-3" rows={4} />
            </div>
             <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="kb_en" className="text-right">Bilimlar bazasi (EN)</Label>
              <Textarea id="kb_en" value={kbEn} onChange={(e) => setKbEn(e.target.value)} className="col-span-3" rows={4} />
            </div>
            {error && <p className="col-span-4 text-sm text-red-500 text-center">{error}</p>}
          </div>
          <div className="flex justify-end">
            <Button type="submit" disabled={loading}>{loading ? "Saqlanmoqda..." : "Saqlash"}</Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}