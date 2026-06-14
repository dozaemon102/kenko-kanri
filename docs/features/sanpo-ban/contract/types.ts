/** Reference types generated from contract/openapi.yaml — not auto-synced */

export type Sex = "male" | "female";

export interface TargetMacros {
  kcal: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
}

export interface Profile extends TargetMacros {
  height_cm: number;
  birth_date: string;
  sex: Sex;
  activity_factor: number;
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

export interface MacroTotals {
  kcal: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
}

export interface DashboardToday {
  date: string;
  targets: TargetMacros;
  intake: MacroTotals;
  burn: {
    walk_kcal: number;
    treadmill_kcal: number;
    strength_kcal: number;
    total_kcal: number;
  };
  remaining: MacroTotals;
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

export interface MealLog {
  id: number;
  log_date: string;
  name: string;
  kcal: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
  food_preset_id: number | null;
  barcode?: string | null;
  logged_at: string;
}

export interface FoodLookup {
  barcode: string;
  name: string;
  kcal: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
  source: "open_food_facts";
  serving_note?: string;
}

export interface MealLogCreate {
  log_date: string;
  name: string;
  kcal: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
  food_preset_id?: number | null;
  barcode?: string | null;
}

export interface HealthSyncRequest {
  date: string;
  steps: number;
  weight_kg?: number | null;
}

export interface WalkSession {
  id: number;
  walked_at: string;
  discovery_note: string | null;
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

export interface ApiError {
  error: {
    code: string;
    message: string;
  };
}
