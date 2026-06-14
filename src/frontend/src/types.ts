export type Sex = "male" | "female";

export interface Profile {
  height_cm: number;
  birth_date: string;
  sex: Sex;
  activity_factor: number;
  target_kcal: number;
  target_protein_g: number;
  target_fat_g: number;
  target_carbs_g: number;
  initial_weight_kg: number;
  setup_completed: boolean;
}

export interface ProfileUpdate {
  height_cm: number;
  birth_date: string;
  sex: Sex;
  activity_factor: number;
  current_weight_kg: number;
  target_kcal?: number;
  target_protein_g?: number;
  target_fat_g?: number;
  target_carbs_g?: number;
  setup_completed?: boolean;
}

export interface DashboardToday {
  date: string;
  targets: { kcal: number; protein_g: number; fat_g: number; carbs_g: number };
  intake: { kcal: number; protein_g: number; fat_g: number; carbs_g: number };
  burn: {
    walk_kcal: number;
    treadmill_kcal: number;
    strength_kcal: number;
    total_kcal: number;
  };
  remaining: { kcal: number; protein_g: number; fat_g: number; carbs_g: number };
  steps: number;
  weight_kg: number | null;
  walk_sessions_today: number;
}

export interface FoodPreset {
  id: number;
  name: string;
  kcal: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
  sort_order: number;
}

export interface WeekSummary {
  start_date: string;
  end_date: string;
  avg_intake_kcal: number;
  avg_steps: number;
  weight_trend: Array<{ date: string; weight_kg: number | null }>;
  counts: {
    walk_sessions: number;
    treadmill_sessions: number;
    strength_sessions: number;
  };
}
