import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

export default function MainLayout({ children }) {
  return (
    <div
      style={{
        display: "flex",
        background: "#0f172a",
        minHeight: "100vh",
        color: "white",
      }}
    >
      <Sidebar />

      <div
        style={{
          flex: 1,
          marginLeft: 260,
        }}
      >
        <Navbar />

        <div
          style={{
            padding: 30,
          }}
        >
          {children}
        </div>
      </div>
    </div>
  );
}
