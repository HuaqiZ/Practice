"use client";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeadCell,
  TableRow,
  Badge,
} from "flowbite-react";
import { useEffect, useState } from "react";

type Run = {
  job_name: string;
  start_time: string;
  status: "success" | "failed" | "running";
};

export default function Home() {
  const [latest, setLatest] = useState<Run[] | null>([]);

  useEffect(() => {
    fetch("http://localhost:8000/runs")
      .then((r) => r.json())
      .then(setLatest)
      .catch(console.error);
  }, []);

  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-50">
      <Table>
        <TableHead>
          <TableRow>
            <TableHeadCell>Job name</TableHeadCell>
            <TableHeadCell>Start Time</TableHeadCell>
            <TableHeadCell>Status</TableHeadCell>
          </TableRow>
        </TableHead>
        <TableBody className="divide-y">
          {latest && latest.map((job, idx) => (
            <TableRow key={idx}>
              <TableCell className="font-medium">{job.job_name}</TableCell>

              <TableCell>{job.start_time}</TableCell>

              <TableCell>
                {job.status === "success" ? (
                  <Badge color="success">Success</Badge>
                ) : (
                  <Badge color="failure">Failed</Badge>
                )}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
