# Section 1: Match info
# Section 2: Player info
create_imports_table = \
	'''CREATE UNLOGGED TABLE IF NOT EXISTS imports(
		date			DATE,
		away_pts		REAL,
		home_pts		REAL,
		away 			TEXT,
		home 			TEXT,
		elevation		REAL,

		player_name		TEXT,
		bbref_endpoint 	TEXT,
		season			REAL,
		age				REAL,
		team_id			TEXT,
		lg				TEXT,
		pos				TEXT,
		g				REAL,
		gs				REAL,
		mp				REAL,
		fg				REAL,
		fga				REAL,
		fg_pct			REAL,
		threep			REAL,
		threepa			REAL,
		threep_pct		REAL,
		twop			REAL,
		twopa			REAL,
		twop_pct		REAL,
		efg_pct			REAL,
		ft				REAL,
		fta				REAL,
		ft_pct			REAL,
		orb				REAL,
		drb				REAL,
		trb				REAL,
		ast				REAL,
		stl				REAL,
		blk				REAL,
		tov				REAL,
		pf				REAL,
		pts				REAL

		);'''

create_season_table =\
	'''CREATE TABLE IF NOT EXISTS season(
		year	SMALLINT	NOT NULL,
		PRIMARY KEY(year)
		);'''
		
create_team_table = \
	'''CREATE TABLE IF NOT EXISTS team(
		team_name				TEXT		NOT NULL,
		team_id					TEXT		NOT NULL,
		home_arena_elevation	REAL		DEFAULT 0,
		created					SMALLINT	DEFAULT 0,
		inactive				SMALLINT 	DEFAULT 3000,
		PRIMARY KEY(team_id)
		);'''

create_player_table = \
	'''CREATE TABLE IF NOT EXISTS player(
		player_id				SERIAL		NOT NULL,
		player_name				TEXT		NOT NULL,
		bbref_endpoint			TEXT		NOT NULL,
		PRIMARY KEY(player_id)
		);'''

create_player_team_table = \
	'''CREATE TABLE IF NOT EXISTS player_team(
		player_id		SERIAL		NOT NULL,
		team_id			TEXT		NOT NULL,
		season			SMALLINT	NOT NULL,
		age				REAL,
		lg				TEXT,
		pos				TEXT,
		g				REAL,
		gs				REAL,
		mp				REAL,
		fg				REAL,
		fga				REAL,
		fg_pct			REAL,
		threep			REAL,
		threepa			REAL,
		threep_pct		REAL,
		twop			REAL,
		twopa			REAL,
		twop_pct		REAL,
		efg_pct			REAL,
		ft				REAL,
		fta				REAL,
		ft_pct			REAL,
		orb				REAL,
		drb				REAL,
		trb				REAL,
		ast				REAL,
		stl				REAL,
		blk				REAL,
		tov				REAL,
		pf				REAL,
		pts				REAL,
		PRIMARY KEY(player_id, team_id, season),
		FOREIGN KEY (player_id) REFERENCES player,
		FOREIGN KEY (team_id) REFERENCES team
		);'''

create_match_table = \
	'''CREATE TABLE IF NOT EXISTS match(
		match_id		SERIAL		NOT NULL,
		date			DATE		NOT NULL,
		away_pts		REAL		NOT NULL,
		home_pts		REAL		NOT NULL,
		away_id 		TEXT		NOT NULL,
		home_id			TEXT		NOT NULL,
		elevation		REAL		DEFAULT 0,
		PRIMARY KEY (match_id),
		FOREIGN KEY (away_id) REFERENCES team,
		FOREIGN KEY (home_id) REFERENCES team
		);'''

create_injury_table = \
	'''CREATE TABLE IF NOT EXISTS injury(
		player_id		SERIAL		NOT NULL,
		match_id		SERIAL		NOT NULL,
		injury			TEXT				,
		PRIMARY KEY (player_id, match_id),
		FOREIGN KEY (player_id) REFERENCES player,
		FOREIGN KEY (match_id) REFERENCES match
		);'''


create_player_performance_import_table = \
	'''CREATE UNLOGGED TABLE IF NOT EXISTS player_performance_imports(
		player_name		TEXT		NOT NULL,
		ts_p			REAL		DEFAULT 0,
		efg_p			REAL		DEFAULT 0,
		three_par		REAL 		DEFAULT 0,
		ftr				REAL		DEFAULT 0,
		orb_p			REAL		DEFAULT 0,
		drb_p			REAL		DEFAULT 0,
		trb_p			REAL		DEFAULT 0,
		ast_p			REAL		DEFAULT 0,
		stl_p			REAL		DEFAULT 0,
		blk_p			REAL		DEFAULT 0,	
		tov_p			REAL		DEFAULT 0,
		usg_p			REAL		DEFAULT 0,
		ortg			REAL		DEFAULT 0,
		drtg 			REAL		DEFAULT 0,
		bpm				REAL		DEFAULT 0,
		match_id		SERIAL		NOT NULL,
		starter 		SMALLINT	DEFAULT 0,
		date			DATE		NOT NULL,
		fg				REAL		DEFAULT 0,
		fga				REAL		DEFAULT 0,
		fg_p			REAL		DEFAULT 0,
		three_p			REAL		DEFAULT 0,
		three_pa		REAL		DEFAULT 0,
		three_p_p		REAL		DEFAULT 0,
		ft				REAL		DEFAULT 0,			
		fta				REAL		DEFAULT 0,
		ft_p			REAL		DEFAULT 0,	
		orb				REAL		DEFAULT 0,
		drb				REAL		DEFAULT 0,
		trb				REAL		DEFAULT 0,
		ast				REAL		DEFAULT 0,
		stl				REAL		DEFAULT 0,
		blk				REAL		DEFAULT 0,		
		tov				REAL		DEFAULT 0,
		pf				REAL		DEFAULT 0,
		pts				REAL		DEFAULT 0,
		pm				REAL		DEFAULT 0
		);'''


create_player_performance_table = \
	'''CREATE TABLE IF NOT EXISTS player_performance(
		player_name		TEXT		NOT NULL,
		ts_p			REAL		DEFAULT 0,
		efg_p			REAL		DEFAULT 0,
		three_par		REAL 		DEFAULT 0,
		ftr				REAL		DEFAULT 0,
		orb_p			REAL		DEFAULT 0,
		drb_p			REAL		DEFAULT 0,
		trb_p			REAL		DEFAULT 0,
		ast_p			REAL		DEFAULT 0,
		stl_p			REAL		DEFAULT 0,
		blk_p			REAL		DEFAULT 0,	
		tov_p			REAL		DEFAULT 0,
		usg_p			REAL		DEFAULT 0,
		ortg			REAL		DEFAULT 0,
		drtg 			REAL		DEFAULT 0,
		bpm				REAL		DEFAULT 0,
		match_id		SERIAL		NOT NULL,
		starter 		SMALLINT	DEFAULT 0,
		date			DATE		NOT NULL,
		fg				REAL		DEFAULT 0,
		fga				REAL		DEFAULT 0,
		fg_p			REAL		DEFAULT 0,
		three_p			REAL		DEFAULT 0,
		three_pa		REAL		DEFAULT 0,
		three_p_p		REAL		DEFAULT 0,
		ft				REAL		DEFAULT 0,			
		fta				REAL		DEFAULT 0,
		ft_p			REAL		DEFAULT 0,	
		orb				REAL		DEFAULT 0,
		drb				REAL		DEFAULT 0,
		trb				REAL		DEFAULT 0,
		ast				REAL		DEFAULT 0,
		stl				REAL		DEFAULT 0,
		blk				REAL		DEFAULT 0,		
		tov				REAL		DEFAULT 0,
		pf				REAL		DEFAULT 0,
		pts				REAL		DEFAULT 0,
		pm				REAL		DEFAULT 0,
		FOREIGN KEY (match_id) REFERENCES match
		);'''