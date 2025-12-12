export default async function Home() {
  const res = await fetch("http://localhost:8000/prices/all", {
    cache: "no-store",
  });

  const data = await res.json();

  return (
    <div className="min-h-screen flex items-center justify-center bg-neutral-50 px-4">
      <div className="w-full max-w-3xl rounded-xl border border-neutral-200 bg-white shadow-sm">
        <table className="w-full text-sm text-left text-neutral-700">
          <thead className="border-b border-neutral-200 bg-neutral-100">
            <tr>
              <th className="px-6 py-3 font-semibold text-neutral-900">Name</th>
              <th className="px-6 py-3 font-semibold text-neutral-900">
                Current Price
              </th>
            </tr>
          </thead>
          <tbody>
            {data.map((item: any) => (
              <tr
                key={item.id}
                className="border-b border-neutral-100 last:border-b-0 hover:bg-neutral-50"
              >
                <td className="px-6 py-4 font-medium text-neutral-900">
                  {item.id}
                </td>
                <td className="px-6 py-4">{item.current_price}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
