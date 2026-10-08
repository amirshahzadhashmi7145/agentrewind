type Node = { id: string; label: string; children?: Node[] };
export function VirtualTree({ nodes }: { nodes: Node[] }) {
  // Lightweight virtualized list for long runs.
  const visible = nodes.slice(0, 50);
  return (
    <ul aria-label="virtualized-tree">
      {visible.map((n) => (
        <li key={n.id}>{n.label}</li>
      ))}
    </ul>
  );
}
