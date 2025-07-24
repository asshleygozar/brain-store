import styles from './page.module.css';

export default function AuthenticationLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<main className={styles.authenticationLayout}>
			<section className={styles.container}>{children}</section>
		</main>
	);
}
