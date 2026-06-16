/** JST (Asia/Tokyo) calendar helpers — avoid UTC toISOString() date drift. */

const JST = "Asia/Tokyo";

export function todayJstIso(): string {
  return new Date().toLocaleDateString("sv-SE", { timeZone: JST });
}

/** Add calendar days to YYYY-MM-DD in JST. */
export function addDaysIso(iso: string, days: number): string {
  const [y, m, d] = iso.split("-").map(Number);
  const utc = Date.UTC(y, m - 1, d, 3, 0, 0);
  return new Date(utc + days * 86_400_000).toLocaleDateString("sv-SE", { timeZone: JST });
}

export function weekdayJa(iso: string): string {
  const dt = new Date(`${iso}T12:00:00+09:00`);
  const label = new Intl.DateTimeFormat("ja-JP", { weekday: "short", timeZone: JST }).format(dt);
  return label.charAt(0);
}

export function formatMonthJa(iso: string): string {
  const [y, m] = iso.split("-").map(Number);
  return `${y}年${m}月`;
}

/** Reset selected date to today when JST midnight passes. Returns true if date changed. */
export function syncTodayIfNeeded(current: string): { date: string; changed: boolean } {
  const today = todayJstIso();
  return { date: today, changed: current !== today };
}
