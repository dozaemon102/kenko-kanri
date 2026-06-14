import type {
  DashboardToday,
  FoodPreset,
  Profile,
  ProfileUpdate,
  WeekSummary,
} from "../types";

const BASE = "/api/v1";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...init?.headers },
    ...init,
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body?.error?.message ?? res.statusText);
  }
  if (res.status === 204) return undefined as T;
  return res.json();
}

export const api = {
  getProfile: () => request<Profile>("/profile"),
  putProfile: (body: ProfileUpdate) =>
    request<Profile>("/profile", { method: "PUT", body: JSON.stringify(body) }),
  getDashboard: (date?: string) =>
    request<DashboardToday>(`/dashboard/today${date ? `?date=${date}` : ""}`),
  getPresets: () => request<FoodPreset[]>("/food-presets"),
  addMealFromPreset: (preset: FoodPreset, logDate: string) =>
    request("/meals", {
      method: "POST",
      body: JSON.stringify({
        log_date: logDate,
        name: preset.name,
        kcal: preset.kcal,
        protein_g: preset.protein_g,
        fat_g: preset.fat_g,
        carbs_g: preset.carbs_g,
        food_preset_id: preset.id,
      }),
    }),
  recordWalk: (note?: string) =>
    request("/walks", {
      method: "POST",
      body: JSON.stringify({ discovery_note: note || null }),
    }),
  syncHealth: (date: string, steps: number, weight_kg?: number) =>
    request("/sync/health", {
      method: "POST",
      body: JSON.stringify({ date, steps, weight_kg }),
    }),
  getWeekSummary: () => request<WeekSummary>("/summary/week"),
  addTreadmill: (minutes: number, machine_kcal?: number) =>
    request("/exercises/treadmill", {
      method: "POST",
      body: JSON.stringify({ minutes, machine_kcal: machine_kcal ?? null }),
    }),
  addStrength: (exercise_code: string, minutes: number) =>
    request("/exercises/strength", {
      method: "POST",
      body: JSON.stringify({ exercise_code, minutes }),
    }),
  getStrengthTemplates: () =>
    request<Array<{ code: string; name: string; met: number }>>(
      "/exercises/strength/templates"
    ),
};

export type { DashboardToday, Profile, WeekSummary };
