# Table: Digital Twin Candidate Action Selection Example

| Candidate Action | Operational Meaning | Projected Mission Assurance | Expected Effect |
|---|---|---:|---|
| Continue | Continue current mission without intervention | 0.58 | Lowest overhead but higher exposure to attack effects |
| Monitor | Continue mission with increased monitoring | 0.62 | Improves awareness but limited recovery impact |
| Reroute | Modify UAV path to reduce navigation or communication risk | 0.71 | Reduces route deviation and avoids degraded areas |
| Reassign | Transfer mission-zone responsibility to healthier UAVs | 0.78 | Highest projected mission assurance in this example |
| Isolate Node | Remove suspected compromised UAV from mission coordination | 0.74 | Improves integrity and limits compromised-node influence |
| Return to Base | Abort affected UAV mission and return to base | 0.66 | Improves safety but reduces mission coverage |

## Manuscript Use

This table should be inserted in the RA-MARS methodology section under digital twin-based adaptive mission continuation.

## Explanation

For each degraded mission state, the RA-MARS digital twin evaluates candidate actions using projected communication reliability, navigation trustworthiness, coverage completion, log integrity, recovery efficiency, and energy overhead. The action with the highest projected Mission Assurance Index is selected unless operational constraints require a safer fallback action.
