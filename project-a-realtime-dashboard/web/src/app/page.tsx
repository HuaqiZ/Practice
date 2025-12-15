import PriceChart from "@/components/chart";

export default async function Home() {
  const res = await fetch("http://localhost:8000/prices/all", {
    cache: "no-store",
  });

  const data = await res.json();

  const labels = data.map((item: any) => item.name);
  const prices = data.map((item: any) => item.current_price);

  return (
    <div className="min-h-screen bg-neutral-50 px-4 py-10 space-y-8">
      <div className="max-w-3xl mx-auto bg-white p-6 rounded-xl border">
        <PriceChart labels={labels} prices={prices} />
      </div>

      <div className="max-w-3xl mx-auto rounded-xl border border-neutral-200 bg-white shadow-sm">
        <table className="w-full text-sm text-left text-neutral-700">
          <thead className="border-b bg-neutral-100">
            <tr>
              <th className="px-6 py-3 font-semibold">Name</th>
              <th className="px-6 py-3 font-semibold">Current Price</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item: any) => (
              <tr key={item.id} className="border-b last:border-b-0">
                <td className="px-6 py-4 font-medium">{item.name}</td>
                <td className="px-6 py-4">{item.current_price}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
