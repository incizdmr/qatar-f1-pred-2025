import pandas as pd


def main():

    clean_df = pd.read_csv("../results/qatar2025_f1_data.csv")

    columns = [
        "AvgQualiPos_2025",
        "AvgRacePos_2025",
        "AvgSprintQualiPos_2025",
        "AvgSprintPos_2025",
    ]

    for col in columns:
        clean_df[col] = clean_df[col].fillna(clean_df[col].mean())

    for col in columns:
        mean = clean_df[col].mean()
        std = clean_df[col].std()
        clean_df[col + "_z"] = (clean_df[col] - mean) / std

    for col in columns:
        clean_df[col + "_z_inv"] = -clean_df[col + "_z"]

    qatar_mean = clean_df["QatarLapTime"].mean()
    qatar_std = clean_df["QatarLapTime"].std()

    clean_df["QatarLapTime_z"] = (clean_df["QatarLapTime"] - qatar_mean) / qatar_std

    clean_df["QatarPace_z_inv"] = -clean_df["QatarLapTime_z"]

    w_quali = 1.0
    w_race = 1.0
    w_sprint_quali = 0.7
    w_sprint = 0.7
    w_qatar = 1.3

    clean_df["QatarPace_z_inv_filled"] = clean_df["QatarPace_z_inv"].fillna(0.0)

    clean_df["PerformanceScore"] = (
        w_quali * clean_df["AvgQualiPos_2025_z_inv"]
        + w_race * clean_df["AvgRacePos_2025_z_inv"]
        + w_sprint_quali * clean_df["AvgSprintQualiPos_2025_z_inv"]
        + w_sprint * clean_df["AvgSprintPos_2025_z_inv"]
        + w_qatar * clean_df["QatarPace_z_inv_filled"]
    )

    results_df = clean_df[["Driver", "Team", "PerformanceScore"]].copy()

    ranking = results_df.sort_values("PerformanceScore", ascending=False).reset_index(
        drop=True
    )

    team_view = ranking[["Team", "Driver", "PerformanceScore"]].sort_values(
        ["Team", "PerformanceScore"], ascending=[True, False]
    )

    team_view["TeamRank"] = team_view.groupby("Team")["PerformanceScore"].rank(
        ascending=False, method="first"
    )

    print("\nTop 15 Drivers:")
    print(ranking.head(15))

    print("\nTeam Rankings:")
    print(team_view)

    ranking.to_csv("../results/qatar2025_driver_predictions.csv", index=False)
    team_view.to_csv("../results/qatar2025_team_view.csv", index=False)
    clean_df.to_csv("../data/clean_df.csv", index=False)


if __name__ == "__main__":
    main()
