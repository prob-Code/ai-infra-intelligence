import { Routes, Route } from "react-router-dom";

import MainLayout from "./layout/MainLayout";

import Dashboard from "./pages/Dashboard";
import Infrastructure from "./pages/Infrastructure";
import Incidents from "./pages/Incidents";
import KnowledgeGraph from "./pages/KnowledgeGraph";
import Analytics from "./pages/Analytics";
import Automation from "./pages/Automation";
import Settings from "./pages/Settings";

export default function App() {
  return (
    <MainLayout>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/infrastructure" element={<Infrastructure />} />
        <Route path="/incidents" element={<Incidents />} />
        <Route path="/knowledge-graph" element={<KnowledgeGraph />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/automation" element={<Automation />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </MainLayout>
  );
}
