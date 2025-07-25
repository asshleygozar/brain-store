'use client';
import styles from 'styles/dashboard/sidebar.module.css';
import { useRouter as navigation } from 'next/navigation';

// MUI Icons
import AccountCircleIcon from '@mui/icons-material/AccountCircle';

export default function SideBar() {
	const navigator = navigation();

	function routerFactory() {
		return {
			profile: function () {
				navigator.push(`/name`);
			},
			message: function () {
				navigator.push(`/messages`);
			},
			theme: function () {
				alert('Theme');
			},
			settings: function () {
				navigator.push(`/settings`);
			},
		};
	}
	return (
		<nav className={styles.container}>
			<ul className={styles.menuContainer}>
				<li>
					<span>
						<AccountCircleIcon style={{ fontSize: '40cp' }}></AccountCircleIcon>
					</span>
					<button onClick={() => routerFactory().profile()}>Profile</button>
				</li>
				<li>
                    <span>

                    </span>
					<button onClick={() => routerFactory().message()}>Messages</button>
				</li>
			</ul>
			<ul className={styles.menuContainer}>
				<li>
                    <span>

                    </span>
					<button onClick={() => routerFactory().theme()}>Light mode</button>
				</li>
				<li>
                    <span>
                        
                    </span>
					<button onClick={() => routerFactory().settings()}>Settings</button>
				</li>
			</ul>
		</nav>
	);
}
