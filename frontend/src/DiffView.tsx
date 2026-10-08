export function DiffView({ left, right }: { left: string; right: string }) {
  return (
    <div aria-label="side-by-side-diff" style={{ display: "grid", gridTemplateColumns: "1fr 1fr" }}>
      <pre>{left}</pre>
      <pre>{right}</pre>
    </div>
  );
}
