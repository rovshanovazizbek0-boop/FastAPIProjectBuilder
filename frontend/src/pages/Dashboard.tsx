import { DashboardLayout } from "@/components/layout/DashboardLayout";

export function DashboardPage() {
  return (
    <DashboardLayout>
      <h2 className="text-2xl font-semibold">Asosiy Panelga Xush Kelibsiz!</h2>
      <p className="text-muted-foreground mt-2">
        Bu yerdan siz o'z botlaringizni boshqarishingiz mumkin.
      </p>
    </DashboardLayout>
  );
}