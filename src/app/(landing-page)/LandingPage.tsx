import styles from './page.module.css';
import Image from 'next/image';
import Link from 'next/link';

export default function LandingPage() {
	return (
		<div className={styles.wrapper}>
			<nav className={styles.navigation}>
				<h1 className={styles.brandLogo}>Blabber</h1>
				<div className={styles.buttonContainer}>
					<Link
						href={'/auth/login'}
						className={styles.link}
					>
						<button className={`${styles.logIn} ${styles.button}`}>
							Log in
						</button>
					</Link>
					<Link
						href={'/auth/signup'}
						className={styles.link}
					>
						<button className={`${styles.signUp} ${styles.button}`}>
							Sign Up
						</button>
					</Link>
				</div>
			</nav>
			<main className={styles.content}>
				<section
					id={'home'}
					className={styles.homePage}
				>
					<h1>
						Chat your <br />
						friends with
						<br /> <span>Blabber!</span>
					</h1>
					<div className={styles.messageImage}>
						<Image
							className={`${styles.homeImage} ${styles.chatUi}`}
							src={'/images/chat_ui.png'}
							alt='Chat user interface'
							width={300}
							height={500}
						/>
						<Image
							className={`${styles.homeImage} ${styles.profileUi}`}
							src={'/images/profile_ui.png'}
							alt='Profile user interface'
							width={380}
							height={500}
						/>
					</div>
				</section>
				<section
					id={'about'}
					className={`${styles.about} ${styles.section}`}
				>
					<h1 className={styles.sectionHeader}>
						A clean fast, and effortless way to chat
					</h1>
					<p>
						Experience seamless messaging with a sleek, modern interface
						designed for clarity and speed. Enjoy real-time conversations,
						smooth animations, and a distraction-free layout that puts your
						words first. Whether you&lsquo;re chatting casually or
						collaborating, every interaction feels intuitive, responsive, and
						beautifully simple.
					</p>
				</section>
				<section
					id={'features'}
					className={`${styles.features} ${styles.section}`}
				>
					<h1 className={styles.sectionHeader}>Experience the style</h1>
					<div className={styles.carousel}>
						<button className={`${styles.backButton} ${styles.carouselButton}`}>
							&lt;
						</button>
						<Image
							className={styles.imageFeature}
							src={'/images/dashboard_feature.png'}
							alt='dashboard'
							width={900}
							height={580}
						/>
						<button className={`${styles.nextButton} ${styles.carouselButton}`}>
							&gt;
						</button>
					</div>
				</section>
			</main>
			<footer className={styles.footer}>
				<div className={styles.footerNavigation}>
					<h1>Blabber</h1>
					<ul>
						<li>
							<a href='#home'>Home</a>
						</li>
						<li>
							<a href='#about'>About</a>
						</li>
						<li>
							<a href='#features'>Features</a>
						</li>
					</ul>
				</div>
				<div className={styles.footerInfo}>
					<p>
						<em> © All rights reserved 2025</em>
					</p>
					<p>
						<strong>Made with ❣️ by Asshley Gozar</strong>
					</p>
				</div>
			</footer>
		</div>
	);
}
