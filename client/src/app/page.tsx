import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.home}>
      <h1>Blabber</h1>
      <h2>Chat with</h2>
    </div>
  );
}
