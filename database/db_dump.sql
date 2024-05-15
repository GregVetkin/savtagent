--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Debian 16.2-1.pgdg120+2)
-- Dumped by pg_dump version 16.2 (Debian 16.2-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: agent; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA agent;


ALTER SCHEMA agent OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cpu_usage; Type: TABLE; Schema: agent; Owner: postgres
--

CREATE TABLE agent.cpu_usage (
    id integer NOT NULL,
    dev_id integer,
    cores real[],
    mean real
);


ALTER TABLE agent.cpu_usage OWNER TO postgres;

--
-- Name: cpu_usage_id_seq; Type: SEQUENCE; Schema: agent; Owner: postgres
--

CREATE SEQUENCE agent.cpu_usage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE agent.cpu_usage_id_seq OWNER TO postgres;

--
-- Name: cpu_usage_id_seq; Type: SEQUENCE OWNED BY; Schema: agent; Owner: postgres
--

ALTER SEQUENCE agent.cpu_usage_id_seq OWNED BY agent.cpu_usage.id;


--
-- Name: disks; Type: TABLE; Schema: agent; Owner: postgres
--

CREATE TABLE agent.disks (
    id integer NOT NULL,
    dev_id integer,
    device character varying(255),
    mountpoint character varying(255),
    total_usage bigint,
    used_usage bigint,
    free_usage bigint,
    percent_usage double precision,
    read_count bigint,
    write_count bigint,
    read_bytes bigint,
    write_bytes bigint
);


ALTER TABLE agent.disks OWNER TO postgres;

--
-- Name: disks_id_seq; Type: SEQUENCE; Schema: agent; Owner: postgres
--

CREATE SEQUENCE agent.disks_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE agent.disks_id_seq OWNER TO postgres;

--
-- Name: disks_id_seq; Type: SEQUENCE OWNED BY; Schema: agent; Owner: postgres
--

ALTER SEQUENCE agent.disks_id_seq OWNED BY agent.disks.id;


--
-- Name: memory; Type: TABLE; Schema: agent; Owner: postgres
--

CREATE TABLE agent.memory (
    id integer NOT NULL,
    dev_id integer,
    ram_total bigint,
    ram_available bigint,
    ram_used bigint,
    ram_percent double precision,
    swap_total bigint,
    swap_free bigint,
    swap_used bigint,
    swap_percent double precision
);


ALTER TABLE agent.memory OWNER TO postgres;

--
-- Name: memory_id_seq; Type: SEQUENCE; Schema: agent; Owner: postgres
--

CREATE SEQUENCE agent.memory_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE agent.memory_id_seq OWNER TO postgres;

--
-- Name: memory_id_seq; Type: SEQUENCE OWNED BY; Schema: agent; Owner: postgres
--

ALTER SEQUENCE agent.memory_id_seq OWNED BY agent.memory.id;


--
-- Name: net_connections; Type: TABLE; Schema: agent; Owner: postgres
--

CREATE TABLE agent.net_connections (
    id integer NOT NULL,
    dev_id integer,
    family integer,
    kind integer,
    laddr_ip character varying(45),
    laddr_port integer,
    raddr_ip character varying(45),
    raddr_port integer,
    status character varying(255),
    pid integer
);


ALTER TABLE agent.net_connections OWNER TO postgres;

--
-- Name: net_connections_id_seq; Type: SEQUENCE; Schema: agent; Owner: postgres
--

CREATE SEQUENCE agent.net_connections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE agent.net_connections_id_seq OWNER TO postgres;

--
-- Name: net_connections_id_seq; Type: SEQUENCE OWNED BY; Schema: agent; Owner: postgres
--

ALTER SEQUENCE agent.net_connections_id_seq OWNED BY agent.net_connections.id;


--
-- Name: net_io; Type: TABLE; Schema: agent; Owner: postgres
--

CREATE TABLE agent.net_io (
    id integer NOT NULL,
    dev_id integer,
    interface character varying(255),
    bytes_sent bigint,
    bytes_recv bigint,
    packets_sent bigint,
    packets_recv bigint
);


ALTER TABLE agent.net_io OWNER TO postgres;

--
-- Name: net_io_id_seq; Type: SEQUENCE; Schema: agent; Owner: postgres
--

CREATE SEQUENCE agent.net_io_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE agent.net_io_id_seq OWNER TO postgres;

--
-- Name: net_io_id_seq; Type: SEQUENCE OWNED BY; Schema: agent; Owner: postgres
--

ALTER SEQUENCE agent.net_io_id_seq OWNED BY agent.net_io.id;


--
-- Name: processes; Type: TABLE; Schema: agent; Owner: postgres
--

CREATE TABLE agent.processes (
    id integer NOT NULL,
    dev_id integer,
    pid integer,
    name character varying,
    username character varying,
    status character varying,
    memory_usage bigint,
    cpu_usage double precision
);


ALTER TABLE agent.processes OWNER TO postgres;

--
-- Name: processes_id_seq; Type: SEQUENCE; Schema: agent; Owner: postgres
--

CREATE SEQUENCE agent.processes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE agent.processes_id_seq OWNER TO postgres;

--
-- Name: processes_id_seq; Type: SEQUENCE OWNED BY; Schema: agent; Owner: postgres
--

ALTER SEQUENCE agent.processes_id_seq OWNED BY agent.processes.id;


--
-- Name: cpu_usage id; Type: DEFAULT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.cpu_usage ALTER COLUMN id SET DEFAULT nextval('agent.cpu_usage_id_seq'::regclass);


--
-- Name: disks id; Type: DEFAULT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.disks ALTER COLUMN id SET DEFAULT nextval('agent.disks_id_seq'::regclass);


--
-- Name: memory id; Type: DEFAULT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.memory ALTER COLUMN id SET DEFAULT nextval('agent.memory_id_seq'::regclass);


--
-- Name: net_connections id; Type: DEFAULT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.net_connections ALTER COLUMN id SET DEFAULT nextval('agent.net_connections_id_seq'::regclass);


--
-- Name: net_io id; Type: DEFAULT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.net_io ALTER COLUMN id SET DEFAULT nextval('agent.net_io_id_seq'::regclass);


--
-- Name: processes id; Type: DEFAULT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.processes ALTER COLUMN id SET DEFAULT nextval('agent.processes_id_seq'::regclass);


--
-- Data for Name: cpu_usage; Type: TABLE DATA; Schema: agent; Owner: postgres
--

COPY agent.cpu_usage (id, dev_id, cores, mean) FROM stdin;
136	5	{31.6,46,49,19.2}	36.45
\.


--
-- Data for Name: disks; Type: TABLE DATA; Schema: agent; Owner: postgres
--

COPY agent.disks (id, dev_id, device, mountpoint, total_usage, used_usage, free_usage, percent_usage, read_count, write_count, read_bytes, write_bytes) FROM stdin;
433	5	sda1	/	124415287296	35695345664	82352676864	30.2	77617	16600	2009306112	657121280
434	5	loop1	/snap/core18/2812	58458112	58458112	0	100	14	0	24576	0
435	5	loop0	/snap/core/16928	109051904	109051904	0	100	464	0	15439872	0
436	5	loop2	/snap/postman/248	181534720	181534720	0	100	23	0	52224	0
\.


--
-- Data for Name: memory; Type: TABLE DATA; Schema: agent; Owner: postgres
--

COPY agent.memory (id, dev_id, ram_total, ram_available, ram_used, ram_percent, swap_total, swap_free, swap_used, swap_percent) FROM stdin;
108	5	8214401024	3904245760	3148218368	52.5	1023406080	1023406080	0	0
\.


--
-- Data for Name: net_connections; Type: TABLE DATA; Schema: agent; Owner: postgres
--

COPY agent.net_connections (id, dev_id, family, kind, laddr_ip, laddr_port, raddr_ip, raddr_port, status, pid) FROM stdin;
311	5	2	1	192.168.0.254	51960	149.154.175.211	443	TIME_WAIT	\N
312	5	2	1	127.0.0.1	38207	\N	\N	LISTEN	7571
313	5	2	1	127.0.0.1	631	\N	\N	LISTEN	\N
314	5	10	1	::	5432	\N	\N	LISTEN	\N
315	5	2	1	192.168.0.254	51098	149.154.167.35	80	TIME_WAIT	\N
316	5	2	1	127.0.0.1	8828	\N	\N	LISTEN	7571
317	5	2	1	192.168.0.254	33966	149.154.167.35	80	TIME_WAIT	\N
318	5	2	2	192.168.0.254	68	192.168.0.1	67	NONE	\N
319	5	10	2	::	48432	\N	\N	NONE	\N
320	5	2	1	192.168.0.254	51100	149.154.167.35	80	TIME_WAIT	\N
321	5	2	1	127.0.0.1	6379	\N	\N	LISTEN	\N
322	5	2	1	192.168.0.254	40824	149.154.167.35	443	TIME_WAIT	\N
323	5	2	1	192.168.0.254	58110	34.107.243.93	443	ESTABLISHED	2402
324	5	2	1	192.168.0.254	59698	149.154.167.35	443	ESTABLISHED	2162
325	5	2	1	192.168.0.254	56428	52.182.143.213	443	ESTABLISHED	7571
326	5	2	1	192.168.0.254	40794	149.154.167.35	443	TIME_WAIT	\N
327	5	2	1	0.0.0.0	22	\N	\N	LISTEN	\N
328	5	2	1	192.168.0.254	57058	140.82.121.5	443	ESTABLISHED	7505
329	5	10	1	::1	631	\N	\N	LISTEN	\N
330	5	2	1	192.168.0.254	59690	149.154.167.35	443	ESTABLISHED	2162
331	5	10	1	::1	5432	::1	53504	ESTABLISHED	\N
332	5	2	1	192.168.0.254	33988	149.154.167.35	80	TIME_WAIT	\N
333	5	2	1	192.168.0.254	40808	149.154.167.35	443	TIME_WAIT	\N
334	5	2	2	0.0.0.0	5353	\N	\N	NONE	\N
335	5	2	1	192.168.0.254	43466	13.107.246.44	443	ESTABLISHED	7505
336	5	2	2	0.0.0.0	631	\N	\N	NONE	\N
337	5	2	1	192.168.0.254	33972	149.154.167.35	80	TIME_WAIT	\N
338	5	2	1	192.168.0.254	60484	152.199.19.160	443	ESTABLISHED	7505
339	5	2	1	192.168.0.254	34602	13.107.5.93	443	ESTABLISHED	7505
340	5	2	1	192.168.0.254	52962	149.154.167.41	443	ESTABLISHED	2162
341	5	2	2	0.0.0.0	50811	\N	\N	NONE	\N
342	5	2	1	0.0.0.0	5432	\N	\N	LISTEN	\N
343	5	2	1	192.168.0.254	51240	20.42.73.31	443	ESTABLISHED	7505
344	5	10	1	::	22	\N	\N	LISTEN	\N
345	5	2	1	192.168.0.254	33512	13.107.42.18	443	ESTABLISHED	7505
346	5	10	2	::	5353	\N	\N	NONE	\N
347	5	10	1	::1	6379	\N	\N	LISTEN	\N
348	5	2	1	192.168.0.254	34608	13.107.5.93	443	TIME_WAIT	\N
349	5	10	1	::1	53504	::1	5432	ESTABLISHED	7902
350	5	2	1	192.168.0.254	40818	149.154.167.35	443	TIME_WAIT	\N
351	5	2	1	192.168.0.254	33992	149.154.167.35	80	TIME_WAIT	\N
352	5	2	1	192.168.0.254	33026	162.159.61.4	443	ESTABLISHED	2402
\.


--
-- Data for Name: net_io; Type: TABLE DATA; Schema: agent; Owner: postgres
--

COPY agent.net_io (id, dev_id, interface, bytes_sent, bytes_recv, packets_sent, packets_recv) FROM stdin;
421	5	lo	116214	116214	628	628
422	5	enp3s0	11080130	96003303	53626	84334
423	5	docker0	0	0	0	0
\.


--
-- Data for Name: processes; Type: TABLE DATA; Schema: agent; Owner: postgres
--

COPY agent.processes (id, dev_id, pid, name, username, status, memory_usage, cpu_usage) FROM stdin;
25103	5	1	systemd	root	sleeping	13074432	0
25104	5	2	kthreadd	root	sleeping	0	0
25105	5	3	rcu_gp	root	idle	0	0
25106	5	4	rcu_par_gp	root	idle	0	0
25107	5	5	slub_flushwq	root	idle	0	0
25108	5	6	netns	root	idle	0	0
25109	5	8	kworker/0:0H-events_highpri	root	idle	0	0
25110	5	9	kworker/u8:0-events_unbound	root	idle	0	0
25111	5	10	mm_percpu_wq	root	idle	0	0
25112	5	11	rcu_tasks_kthread	root	idle	0	0
25113	5	12	rcu_tasks_rude_kthread	root	idle	0	0
25114	5	13	rcu_tasks_trace_kthread	root	idle	0	0
25115	5	14	ksoftirqd/0	root	sleeping	0	0
25116	5	15	rcu_preempt	root	idle	0	0.25
25117	5	16	migration/0	root	sleeping	0	0
25118	5	18	cpuhp/0	root	sleeping	0	0
25119	5	19	cpuhp/1	root	sleeping	0	0
25120	5	20	migration/1	root	sleeping	0	0
25121	5	21	ksoftirqd/1	root	sleeping	0	0
25122	5	23	kworker/1:0H-events_highpri	root	idle	0	0
25123	5	24	cpuhp/2	root	sleeping	0	0
25124	5	25	migration/2	root	sleeping	0	0
25125	5	26	ksoftirqd/2	root	sleeping	0	0
25126	5	28	kworker/2:0H-events_highpri	root	idle	0	0
25127	5	29	cpuhp/3	root	sleeping	0	0
25128	5	30	migration/3	root	sleeping	0	0
25129	5	31	ksoftirqd/3	root	sleeping	0	0
25130	5	38	kdevtmpfs	root	sleeping	0	0
25131	5	39	inet_frag_wq	root	idle	0	0
25132	5	40	kauditd	root	sleeping	0	0
25133	5	41	khungtaskd	root	sleeping	0	0
25134	5	42	oom_reaper	root	sleeping	0	0
25135	5	43	writeback	root	idle	0	0
25136	5	44	kcompactd0	root	sleeping	0	0
25137	5	45	ksmd	root	sleeping	0	0
25138	5	46	khugepaged	root	sleeping	0	0
25139	5	47	kintegrityd	root	idle	0	0
25140	5	48	kblockd	root	idle	0	0
25141	5	49	blkcg_punt_bio	root	idle	0	0
25142	5	50	tpm_dev_wq	root	idle	0	0
25143	5	51	edac-poller	root	idle	0	0
25144	5	52	devfreq_wq	root	idle	0	0
25145	5	53	kworker/0:1H-events_highpri	root	idle	0	0
25146	5	54	kswapd0	root	sleeping	0	0
25147	5	62	kthrotld	root	idle	0	0
25148	5	64	acpi_thermal_pm	root	idle	0	0
25149	5	65	kworker/0:2-events	root	idle	0	0
25150	5	66	mld	root	idle	0	0
25151	5	67	ipv6_addrconf	root	idle	0	0
25152	5	72	kstrp	root	idle	0	0
25153	5	77	zswap-shrink	root	idle	0	0
25154	5	78	kworker/u9:0-i915_flip	root	idle	0	0
25155	5	128	kworker/2:1H-events_highpri	root	idle	0	0
25156	5	135	kworker/3:1H-kblockd	root	idle	0	0
25157	5	136	kworker/1:1H-events_highpri	root	idle	0	0
25158	5	157	ata_sff	root	idle	0	0
25159	5	159	scsi_eh_0	root	sleeping	0	0
25160	5	160	scsi_tmf_0	root	idle	0	0
25161	5	161	scsi_eh_1	root	sleeping	0	0
25162	5	162	scsi_tmf_1	root	idle	0	0
25163	5	163	scsi_eh_2	root	sleeping	0	0
25164	5	164	scsi_tmf_2	root	idle	0	0
25165	5	165	scsi_eh_3	root	sleeping	0	0
25166	5	166	scsi_tmf_3	root	idle	0	0
25167	5	169	card0-crtc0	root	sleeping	0	0
25168	5	170	card0-crtc1	root	sleeping	0	0
25169	5	171	card0-crtc2	root	sleeping	0	0
25170	5	184	kworker/3:2H-kblockd	root	idle	0	0
25171	5	225	jbd2/sda1-8	root	sleeping	0	0
25172	5	226	ext4-rsv-conver	root	idle	0	0
25173	5	278	systemd-journald	root	sleeping	38346752	0
25174	5	303	systemd-udevd	root	sleeping	7647232	0
25175	5	352	watchdogd	root	sleeping	0	0
25176	5	366	led_workqueue	root	idle	0	0
25177	5	380	cryptd	root	idle	0	0
25178	5	482	systemd-timesyncd	systemd-timesync	sleeping	7069696	0
25179	5	555	accounts-daemon	root	sleeping	9846784	0
25180	5	557	avahi-daemon	avahi	sleeping	3997696	0
25181	5	558	cron	root	sleeping	2789376	0
25182	5	559	dbus-daemon	messagebus	sleeping	6868992	0
25183	5	561	low-memory-monitor	root	sleeping	6410240	0
25184	5	562	polkitd	polkitd	sleeping	13357056	0
25185	5	563	power-profiles-daemon	root	sleeping	9199616	0
25186	5	564	snapd	root	sleeping	40255488	0
25187	5	565	switcheroo-control	root	sleeping	10551296	0
25188	5	566	systemd-logind	root	sleeping	8159232	0
25189	5	567	udisksd	root	sleeping	16269312	0
25190	5	568	avahi-daemon	avahi	sleeping	372736	0
25191	5	601	psimon	root	sleeping	0	0
25192	5	602	NetworkManager	root	sleeping	22597632	0
25193	5	613	wpa_supplicant	root	sleeping	5984256	0
25194	5	618	ModemManager	root	sleeping	12468224	0
25195	5	644	cupsd	root	sleeping	9109504	0
25196	5	646	redis-server	redis	sleeping	16908288	0.25
25197	5	659	containerd	root	sleeping	46219264	0
25198	5	670	gdm3	root	sleeping	11337728	0
25199	5	671	sshd	root	sleeping	8454144	0
25200	5	718	postgres	postgres	sleeping	30732288	0
25201	5	750	postgres	postgres	sleeping	9003008	0
25202	5	751	postgres	postgres	sleeping	6189056	0
25203	5	757	postgres	postgres	sleeping	10743808	0
25204	5	758	postgres	postgres	sleeping	9027584	0
25205	5	759	postgres	postgres	sleeping	7168000	0
25206	5	794	rtkit-daemon	rtkit	sleeping	1585152	0
25207	5	888	cups-browsed	root	sleeping	15417344	0
25208	5	893	dockerd	root	sleeping	90849280	0
25209	5	967	upowerd	root	sleeping	8790016	0
25210	5	1198	colord	colord	sleeping	15859712	0
25211	5	1396	kworker/u9:1	root	idle	0	0
25212	5	1453	gdm-session-worker	root	sleeping	11780096	0
25213	5	1467	systemd	greg	sleeping	11845632	0
25214	5	1471	(sd-pam)	greg	sleeping	3784704	0
25215	5	1486	pipewire	greg	sleeping	13275136	0
25216	5	1488	wireplumber	greg	sleeping	19099648	0
25217	5	1490	pipewire-pulse	greg	sleeping	16965632	0
25218	5	1493	gnome-keyring-daemon	greg	sleeping	13987840	0
25219	5	1495	dbus-daemon	greg	sleeping	6127616	0
25220	5	1502	gvfsd	greg	sleeping	10117120	0
25221	5	1518	gvfsd-fuse	greg	sleeping	8347648	0
25222	5	1532	tracker-miner-fs-3	greg	sleeping	94904320	0
25223	5	1538	gdm-wayland-session	greg	sleeping	8122368	0
25224	5	1544	gnome-session-binary	greg	sleeping	18759680	0
25225	5	1592	gcr-ssh-agent	greg	sleeping	5636096	0
25226	5	1593	gnome-session-ctl	greg	sleeping	7204864	0
25227	5	1594	ssh-agent	greg	sleeping	5222400	0
25228	5	1605	gnome-session-binary	greg	sleeping	22609920	0
25229	5	1623	gnome-shell	greg	sleeping	283283456	0.475
25230	5	1624	at-spi-bus-launcher	greg	sleeping	9936896	0
25231	5	1630	dbus-daemon	greg	sleeping	4857856	0
25232	5	1660	gvfs-udisks2-volume-monitor	greg	sleeping	16859136	0
25233	5	1671	gvfs-mtp-volume-monitor	greg	sleeping	8712192	0
25234	5	1675	gvfs-gphoto2-volume-monitor	greg	sleeping	9179136	0
25235	5	1679	gvfs-goa-volume-monitor	greg	sleeping	10731520	0
25236	5	1683	goa-daemon	greg	sleeping	41570304	0
25237	5	1690	goa-identity-service	greg	sleeping	11214848	0
25238	5	1695	gvfs-afc-volume-monitor	greg	sleeping	10371072	0
25239	5	1723	xdg-permission-store	greg	sleeping	9084928	0
25240	5	1725	gnome-shell-calendar-server	greg	sleeping	19062784	0
25241	5	1739	evolution-source-registry	greg	sleeping	50012160	0
25242	5	1757	evolution-calendar-factory	greg	sleeping	30621696	0
25243	5	1761	gvfsd-trash	greg	sleeping	12783616	0
25244	5	1774	evolution-addressbook-factory	greg	sleeping	32833536	0
25245	5	1777	gjs	greg	sleeping	31698944	0
25246	5	1779	at-spi2-registryd	greg	sleeping	11673600	0
25247	5	1800	sh	greg	sleeping	937984	0
25248	5	1802	gsd-a11y-settings	greg	sleeping	8577024	0
25249	5	1803	gsd-color	greg	sleeping	26021888	0
25250	5	1804	gsd-datetime	greg	sleeping	14008320	0
25251	5	1805	gsd-housekeeping	greg	sleeping	9568256	0
25252	5	1806	gsd-keyboard	greg	sleeping	24625152	0
25253	5	1808	gsd-media-keys	greg	sleeping	32104448	0
25254	5	1809	gsd-power	greg	sleeping	31084544	0
25255	5	1810	gsd-print-notifications	greg	sleeping	13758464	0
25256	5	1812	gsd-rfkill	greg	sleeping	10629120	0
25257	5	1814	gsd-screensaver-proxy	greg	sleeping	8282112	0
25258	5	1815	gsd-sharing	greg	sleeping	14757888	0
25259	5	1816	gnome-software	greg	sleeping	156815360	0
25260	5	1818	gsd-smartcard	greg	sleeping	12558336	0
25261	5	1820	gsd-sound	greg	sleeping	13864960	0
25262	5	1821	gsd-usb-protection	greg	sleeping	11223040	0
25263	5	1824	gsd-wacom	greg	sleeping	25415680	0
25264	5	1827	gsd-disk-utility-notify	greg	sleeping	8790016	0
25265	5	1828	evolution-alarm-notify	greg	sleeping	75300864	0
25266	5	1830	ibus-daemon	greg	sleeping	14442496	0
25267	5	1960	dconf-service	greg	sleeping	5898240	0
25268	5	1961	gjs	greg	sleeping	31621120	0
25269	5	1975	ibus-dconf	greg	sleeping	11513856	0
25270	5	1976	gsd-printer	greg	sleeping	16470016	0
25271	5	1979	ibus-extension-gtk3	greg	sleeping	33558528	0
25272	5	1996	ibus-portal	greg	sleeping	7311360	0
25273	5	2040	ibus-engine-simple	greg	sleeping	9334784	0
25274	5	2043	gvfsd-metadata	greg	sleeping	8642560	0
25275	5	2044	xdg-desktop-portal	greg	sleeping	19165184	0
25276	5	2050	xdg-document-portal	greg	sleeping	11665408	0
25277	5	2060	fusermount3	greg	sleeping	983040	0
25278	5	2073	xdg-desktop-portal-gnome	greg	sleeping	28491776	0
25279	5	2102	xdg-desktop-portal-gtk	greg	sleeping	26148864	0
25280	5	2114	fwupd	root	sleeping	125870080	0
25281	5	2162	telegram-desktop	greg	sleeping	805089280	0
25282	5	2241	gnome-terminal-server	greg	sleeping	51974144	0
25283	5	2270	bash	greg	sleeping	5152768	0
25284	5	2402	firefox-esr	greg	sleeping	480366592	0
25285	5	2406	Xwayland	greg	sleeping	102633472	0
25286	5	2413	gsd-xsettings	greg	sleeping	84013056	0
25287	5	2435	ibus-x11	greg	sleeping	25362432	0
25288	5	2492	Socket Process	greg	sleeping	42143744	0
25289	5	2539	Privileged Cont	greg	sleeping	126861312	0
25290	5	2587	WebExtensions	greg	sleeping	98820096	0
25291	5	6168	sd_espeak-ng	greg	sleeping	10334208	0
25292	5	6173	sd_dummy	greg	sleeping	5664768	0
25293	5	6179	speech-dispatcher	greg	sleeping	9248768	0
25294	5	6338	RDD Process	greg	sleeping	111554560	0
25295	5	6340	Utility Process	greg	sleeping	50995200	0
25296	5	6434	kworker/3:3-events	root	idle	0	0
25297	5	6640	kworker/2:2-mm_percpu_wq	root	idle	0	0
25298	5	6935	kworker/1:0-events	root	idle	0	0
25299	5	6944	kworker/u8:1-events_unbound	root	idle	0	0
25300	5	6985	Web Content	greg	sleeping	72937472	0
25301	5	7178	kworker/2:0-cgroup_destroy	root	idle	0	0
25302	5	7179	kworker/3:0-events	root	idle	0	0
25303	5	7186	Web Content	greg	sleeping	73424896	0
25304	5	7206	kworker/0:0-events	root	idle	0	0
25305	5	7236	Web Content	greg	sleeping	70586368	0
25306	5	7296	kworker/1:1-ata_sff	root	idle	0	0
25307	5	7366	kworker/1:2-ata_sff	root	idle	0	0
25308	5	7376	kworker/2:1-cgroup_destroy	root	idle	0	0
25309	5	7377	kworker/u8:2-flush-8:0	root	idle	0	0
25310	5	7440	kworker/u8:3-flush-8:0	root	idle	0	0
25311	5	7460	code	greg	sleeping	180137984	0.475
25312	5	7464	code	greg	sleeping	47767552	0
25313	5	7465	code	greg	sleeping	47996928	0
25314	5	7467	code	greg	sleeping	11972608	0
25315	5	7481	chrome_crashpad_handler	greg	sleeping	2867200	0
25316	5	7496	code	greg	sleeping	180592640	1.15
25317	5	7505	code	greg	sleeping	68190208	0.225
25318	5	7527	code	greg	sleeping	440676352	0.925
25319	5	7561	code	greg	sleeping	100687872	0.225
25320	5	7571	code	greg	sleeping	229515264	0.7
25321	5	7581	code	greg	sleeping	133029888	0
25322	5	7582	code	greg	sleeping	91418624	0
25323	5	7631	bash	greg	sleeping	5263360	0
25324	5	7646	bash	greg	sleeping	5197824	0
25325	5	7749	code	greg	sleeping	208846848	0
25326	5	7764	bash	greg	sleeping	5300224	0
25327	5	7862	bash	greg	sleeping	5320704	0
25328	5	7902	python	greg	running	28102656	2.075
25329	5	7906	postgres	postgres	sleeping	17477632	0
\.


--
-- Name: cpu_usage_id_seq; Type: SEQUENCE SET; Schema: agent; Owner: postgres
--

SELECT pg_catalog.setval('agent.cpu_usage_id_seq', 136, true);


--
-- Name: disks_id_seq; Type: SEQUENCE SET; Schema: agent; Owner: postgres
--

SELECT pg_catalog.setval('agent.disks_id_seq', 436, true);


--
-- Name: memory_id_seq; Type: SEQUENCE SET; Schema: agent; Owner: postgres
--

SELECT pg_catalog.setval('agent.memory_id_seq', 108, true);


--
-- Name: net_connections_id_seq; Type: SEQUENCE SET; Schema: agent; Owner: postgres
--

SELECT pg_catalog.setval('agent.net_connections_id_seq', 352, true);


--
-- Name: net_io_id_seq; Type: SEQUENCE SET; Schema: agent; Owner: postgres
--

SELECT pg_catalog.setval('agent.net_io_id_seq', 423, true);


--
-- Name: processes_id_seq; Type: SEQUENCE SET; Schema: agent; Owner: postgres
--

SELECT pg_catalog.setval('agent.processes_id_seq', 25329, true);


--
-- Name: cpu_usage cpu_usage_pkey; Type: CONSTRAINT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.cpu_usage
    ADD CONSTRAINT cpu_usage_pkey PRIMARY KEY (id);


--
-- Name: disks disks_pkey; Type: CONSTRAINT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.disks
    ADD CONSTRAINT disks_pkey PRIMARY KEY (id);


--
-- Name: memory memory_pkey; Type: CONSTRAINT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.memory
    ADD CONSTRAINT memory_pkey PRIMARY KEY (id);


--
-- Name: net_connections net_connections_pkey; Type: CONSTRAINT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.net_connections
    ADD CONSTRAINT net_connections_pkey PRIMARY KEY (id);


--
-- Name: net_io net_io_pkey; Type: CONSTRAINT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.net_io
    ADD CONSTRAINT net_io_pkey PRIMARY KEY (id);


--
-- Name: processes processes_pkey; Type: CONSTRAINT; Schema: agent; Owner: postgres
--

ALTER TABLE ONLY agent.processes
    ADD CONSTRAINT processes_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

