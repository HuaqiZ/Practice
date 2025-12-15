"use client";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  LogarithmicScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";
import type { ChartOptions } from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  LogarithmicScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const options: ChartOptions<"bar"> = {
  responsive: true,
  plugins: {
    legend: { position: "top" as const },
    title: {
      display: true,
      text: "Prices",
    },
  },
  scales: {
    y: {
      type: "logarithmic",
    },
  },
};

type Props = {
  labels: string[];
  prices: number[];
};

export default function PriceChart({ labels, prices }: Props) {
  const data = {
    labels,
    datasets: [
      {
        label: "Current Price",
        data: prices,
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
    ],
  };

  return <Bar options={options} data={data} />;
}
