/** Reference types from contract/openapi.yaml v3 — not auto-synced */

export type Sex = "male" | "female";

export type HistoryMetric =
  | "balance"
  | "weight"
  | "intake"
  | "bmr"
  | "exercise"
  | "steps"
  | "body_fat_pct"
  | "bmi"
  | "lbm";

export type HistoryPeriod = "day" | "week" | "month" | "year";

export type BmrStatus = "ok" | "lbm_missing";

export type BodyCompositionSource = "today" | "latest" | "none";

export interface Profile {
  height_cm: number;
  birth_date: string;
  sex: Sex;
  neat_kcal: number;
  tef_rate: number;
  initial_weight_kg: number;
  setup_completed: boolean;
}

export interface ProfileUpdate {
  height_cm: number;
  birth_date: string;
  sex: Sex;
  current_weight_kg: number;
  neat_kcal?: number;
  tef_rate?: number;
  setup_completed?: boolean;
}

export interface BalanceBreakdown {
  intake_kcal: number;
  bmr_kcal: number | null;
  neat_kcal: number;
  exercise_kcal: number;
  tef_kcal: number;
}

export interface BalanceInfo {
  value: number | null;
  computable: boolean;
  breakdown: BalanceBreakdown;
}

export interface DashboardCards {
  weight_kg: number | null;
  intake_kcal: number;
  bmr_kcal: number | null;
  exercise_kcal: number;
  steps: number;
  body_fat_pct: number | null;
  bmi: number | null;
  lbm_kg: number | null;
}

export interface DashboardTop {
  date: string;
  balance: BalanceInfo;
  cards: DashboardCards;
  bmr_status: BmrStatus;
  body_composition_source: BodyCompositionSource;
}

export interface HistoryPoint {
  label: string;
  start_date: string;
  end_date: string;
  value: number | null;
}

export interface DashboardHistory {
  metric: HistoryMetric;
  period: HistoryPeriod;
  anchor_date: string;
  points: HistoryPoint[];
}

export interface MacroTotals {
  kcal: number;
  protein_g: number;
  fat_g: number;
  carbs_g: number;
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

export interface WeightLog {
  id: number;
  weight_kg: number;
  bmi: number | null;
  lbm_kg: number | null;
  body_fat_pct: number | null;
  source: "manual" | "shortcuts";
  logged_at: string;
}

export interface HealthSyncRequest {
  date: string;
  steps?: number | null;
  weight_kg?: number | null;
  bmi?: number | null;
  lbm_kg?: number | null;
  body_fat_pct?: number | null;
}

export interface TreadmillLog {
  id: number;
  logged_at: string;
  minutes: number;
  speed_kmh: number | null;
  incline_pct: number | null;
  machine_kcal: number | null;
  calculated_kcal: number;
}

export interface StrengthLog {
  id: number;
  logged_at: string;
  exercise_code: string;
  minutes: number;
  calculated_kcal: number;
}

export interface ApiError {
  error: {
    code: string;
    message: string;
  };
}
