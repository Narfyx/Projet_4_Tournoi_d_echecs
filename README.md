        try:
            tournament_dir = f"data/tournaments_play/{tournament['name']}/"
            match_files = [
                f for f in os.listdir(tournament_dir) if f.startswith("round") and f.endswith("_matches.json")
            ]
            round_numbers = []
            for filename in match_files:
                round_number = int(filename.split('_')[1])  # Extraire le numéro du round du nom de fichier
                round_numbers.append(round_number)
            max_round = max(round_numbers)
            matches_data = []
            # Parcourir tous les fichiers de résultats des matchs
            for match_file in match_files:
                with open(os.path.join(tournament_dir, match_file), "r", encoding="utf-8") as f:
                    matches_data.append(json.load(f))
            player_scores = {} # exemple {'AB12345': 1, 'AC12345': 4} -> identification_code : score
            # Parcours des données de match
            for matches in matches_data:
                for match in matches:
                    # Obtention des informations des joueurs et de leurs scores dans le match
                    player1_info = match['player1']
                    player2_info = match['player2']
                    # Mise à jour du score le plus élevé de chaque joueur

                    player_scores[player1_info['identification_code']] = max(
                        player_scores.get(
                            player1_info['identification_code'], float('-inf')), player1_info['score'])

                    player_scores[player2_info['identification_code']] = max(
                        player_scores.get(
                            player2_info['identification_code'], float('-inf')), player2_info['score'])

            round_instance = Round(players=PlayerModel().players_data, tournament=tournament)
            round_instance.set_score()
            new_list_players = []
            for player in round_instance.list_players:
                if player['identification_code'] in player_scores:
                    score_player = player_scores[player['identification_code']]
                    player['score'] = score_player
                    new_list_players.append(player)
            round_instance.list_players = new_list_players
            round_instance.new_combinaison_by_score()
            round_instance.actual_round = max_round
        except FileNotFoundError:
            round_instance = Round(players=PlayerModel().players_data, tournament=tournament)
            round_instance.set_score()
        return round_instance