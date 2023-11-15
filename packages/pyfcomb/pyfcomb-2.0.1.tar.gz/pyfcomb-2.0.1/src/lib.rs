use pyo3::prelude::*;
use std::cmp::Ordering;

#[pyclass]
#[derive(Debug,Clone)]
pub struct RFrequency {
    pub frequency_number: i32,
    pub frequency: f64,
    pub amplitude: f64,
}

impl RFrequency {
}

//override equality operator
impl PartialEq for RFrequency {
    fn eq(&self, other: &RFrequency) -> bool {
        self.frequency == other.frequency
    }
}

//override less than operator
impl PartialOrd for RFrequency {
    fn partial_cmp(&self, other: &RFrequency) -> Option<Ordering> {
        self.frequency.partial_cmp(&other.frequency)
    }
}

struct RFrequencyCompositionComponent {
    factor: i32,
}

//Imlement equality and ordering for RFrequencyCompositionComponent
impl PartialEq for RFrequencyCompositionComponent {
    fn eq(&self, other: &RFrequencyCompositionComponent) -> bool {
        self.factor == other.factor
    }
}

impl PartialOrd for RFrequencyCompositionComponent {
    fn partial_cmp(&self, other: &RFrequencyCompositionComponent) -> Option<Ordering> {
        self.factor.partial_cmp(&other.factor)
    }
}

pub struct RFrequencyComposition {
    pub component: RFrequency,
    pub composition_string: String,
}

fn check_for_composition(fnum: i32, freq: f64, ampl: f64, maxdepth: i32, accuracy: f64, found_frequency_objects: &Vec<RFrequency>) -> RFrequencyComposition {
    let mut composition_strings: Vec<String> = vec![];
    let mut used_depth = maxdepth;

    for found_frequency_object in found_frequency_objects {
        for k in 1..=used_depth {
            let diff = ((k as f64) * found_frequency_object.frequency - freq).abs();
            if diff <= accuracy {
                let composition = format!(
                    "f{}={}f{} {:.2} {:.2} {:.2}",
                    fnum,
                    k,
                    found_frequency_object.frequency_number,
                    diff,
                    0.01 * found_frequency_object.amplitude.powi(k),
                    ampl / found_frequency_object.amplitude.powi(k)
                );

                composition_strings.push(composition);
            }
        }
    }

    used_depth = used_depth - 1;
    let size_of_frequency_array = found_frequency_objects.len() as i32;


    // check two-component compositions
    for i in 0..size_of_frequency_array {
        //	for (int j=i+1; j<size; j++) {
        // we need 0 for - combinations, so we have duplicates for + combis
        for j in 0..size_of_frequency_array {
            if i == j {
                continue;
            }

            // i and j define the frequency indices
            // k and l define the depth of the combination
            for k in 1..=used_depth {
                for l in 1..=used_depth {
                    let mut diff = ((k as f64) * found_frequency_objects[i as usize].frequency + (l as f64) * found_frequency_objects[j as usize].frequency - freq).abs();
                    if diff <= accuracy {
                        let composition = format!(
                            "f{}={}f{}+{}f{} {:.2} {:.2} {:.2}",
                            fnum,
                            k,
                            found_frequency_objects[i as usize].frequency_number,
                            l,
                            found_frequency_objects[j as usize].frequency_number,
                            diff,
                            0.01 * found_frequency_objects[i as usize].amplitude.powi(k) * 0.01 * found_frequency_objects[j as usize].amplitude.powi(l),
                            ampl / found_frequency_objects[i as usize].amplitude.powi(k) / found_frequency_objects[j as usize].amplitude.powi(l)
                        );

                        composition_strings.push(composition);
                    }

                    diff = ((k as f64) * found_frequency_objects[i as usize].frequency - (l as f64) * found_frequency_objects[j as usize].frequency - freq).abs();

                    if diff <= accuracy {
                        let composition = format!(
                            "f{}={}f{}-{}f{} {:.2} {:.2} {:.2}",
                            fnum,
                            k,
                            found_frequency_objects[i as usize].frequency_number,
                            l,
                            found_frequency_objects[j as usize].frequency_number,
                            diff,
                            0.01 * found_frequency_objects[i as usize].amplitude.powi(k) * 0.01 * found_frequency_objects[j as usize].amplitude.powi(l),
                            ampl / found_frequency_objects[i as usize].amplitude.powi(k) / found_frequency_objects[j as usize].amplitude.powi(l)
                        );

                        composition_strings.push(composition);
                    }
                }
            }
        }
    }

    // check three-component compositions
    used_depth = used_depth - 1;

    // Check three-component compositions
    for i in 0..size_of_frequency_array {
        for j in 0..size_of_frequency_array {
            for h in 0..size_of_frequency_array {
                if i == j || j == h || i == h {
                    continue;
                }
                for k in 1..=used_depth {
                    for l in 1..=used_depth {
                        for m in 1..=used_depth {
                            let combinations = [
                                (k as f64, l as f64, m as f64), // k + l + m
                                (k as f64, l as f64, -(m as f64)), // k + l - m
                                (k as f64, -(l as f64), m as f64), // k - l + m
                                (k as f64, -(l as f64), -(m as f64)), // k - l - m
                            ];

                            for (kf, lf, mf) in &combinations {
                                let diff = (kf * found_frequency_objects[i as usize].frequency + lf * found_frequency_objects[j as usize].frequency + mf * found_frequency_objects[h as usize].frequency - freq).abs();
                                if diff <= accuracy {
                                    let composition = format!(
                                        "f{}={}f{}{}{}f{}{}{}f{} {:.2} {:.2} {:.2}",
                                        fnum,
                                        k, found_frequency_objects[i as usize].frequency_number,
                                        if *lf > 0.0 { "+" } else { "-" }, l.abs(), found_frequency_objects[j as usize].frequency_number,
                                        if *mf > 0.0 { "+" } else { "-" }, m.abs(), found_frequency_objects[h as usize].frequency_number,
                                        diff,
                                        0.01 * found_frequency_objects[i as usize].amplitude.powi(*kf as i32) * found_frequency_objects[j as usize].amplitude.powi(*lf as i32).abs() * found_frequency_objects[h as usize].amplitude.powi(*mf as i32).abs(),
                                        ampl / (found_frequency_objects[i as usize].amplitude.powi(*kf as i32) * found_frequency_objects[j as usize].amplitude.powi(*lf as i32).abs() * found_frequency_objects[h as usize].amplitude.powi(*mf as i32).abs())
                                    );

                                    composition_strings.push(composition);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    // Select the simplest composition
    let mut scompo = String::new();
    let mut full = String::new();
    let mut best_weight = -1.0;
    let mut best_offset = -1.0;
    let mut best_mufactor = -1.0;

    // Sort the composition strings
    composition_strings.sort_unstable();

    for composition in &composition_strings {
        let parts: Vec<&str> = composition.split_whitespace().collect();
        if parts.len() < 4 {
            continue; // Skip if the format is not as expected
        }

        let sc = parts[0];
        let df = parts[1].parse::<f64>().unwrap_or(0.0);
        let iw = parts[2].parse::<f64>().unwrap_or(0.0);
        let mu = parts[3].parse::<f64>().unwrap_or(0.0);

        full.push(';');
        full.push_str(sc);

        if iw > best_weight {
            best_weight = iw;
            scompo = sc.to_string();
            best_offset = df;
            best_mufactor = mu;
        }
    }

    scompo.push_str(&full);

    RFrequencyComposition {
        component: RFrequency {
            frequency_number: fnum,
            frequency: freq,
            amplitude: ampl,
        },
        composition_string: scompo,
    }
}

#[pyfunction]
fn r_get_combinations(vec: Vec<RFrequency>, combo_depth: i32, accuracy: f64) -> (Vec<String>, Vec<String>) {
    let mut component_strings: Vec<String> = vec![];
    let mut independent_strings: Vec<String> = vec![];
    let mut found_frequency_objects: Vec<RFrequency> = vec![];

    for data in vec {
        let composition = check_for_composition(data.frequency_number, data.frequency, data.amplitude, combo_depth, accuracy, &found_frequency_objects);
        if !composition.composition_string.is_empty() {
            component_strings.push(composition.composition_string);
        } else {
            found_frequency_objects.push(data.clone());
            independent_strings.push(format!("f{}", data.frequency_number));
        }
    }

    (component_strings, independent_strings)
}

#[pymodule]
#[pyo3(name="rfcomb")]
fn rfcomb(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<RFrequency>()?;
    m.add_function(wrap_pyfunction!(r_get_combinations, m)?)?;
    Ok(())
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rfrequency_creation() {
        let freq = RFrequency::new(440.0, 1, 0.5);
        assert_eq!(freq.frequency, 440.0);
        assert_eq!(freq.frequency_number, 1);
        assert_eq!(freq.amplitude, 0.5);
    }

    #[test]
    fn test_rfrequency_equality() {
        let freq1 = RFrequency::new(440.0, 1, 0.5);
        let freq2 = RFrequency::new(440.0, 2, 0.3);
        let freq3 = RFrequency::new(880.0, 1, 0.5);

        assert_eq!(freq1, freq2);
        assert_ne!(freq1, freq3);
    }

    #[test]
    fn test_rfrequency_ordering() {
        let freq1 = RFrequency::new(440.0, 1, 0.5);
        let freq2 = RFrequency::new(880.0, 2, 0.3);

        assert!(freq1 < freq2);
        assert!(freq2 > freq1);
    }

    // Test to check if a single frequency close to the target is identified correctly
    #[test]
    fn test_one_component_composition() {
        // Setup
        let fnum = 1; // Arbitrary frequency number
        let target_freq = 100.0; // Target frequency
        let ampl = 1.0; // Amplitude
        let maxdepth = 1; // Depth for one-component composition
        let accuracy = 0.5; // Accuracy range

        // Create an RFrequency array with one element close to the target frequency
        let found_frequency_objects = vec![
            RFrequency {
                frequency_number: 2,
                frequency: 99.5, // Close to the target frequency
                amplitude: 1.0,
            },
        ];

        // Call check_for_composition
        let composition = check_for_composition(fnum, target_freq, ampl, maxdepth, accuracy, &found_frequency_objects);

        // Assert
        assert_eq!(composition.composition_string, "f1=1f2;f1=1f2");
        // This assertion checks if the correct composition string is returned
    }

    #[test]
    fn test_two_component_composition() {
        // Setup
        let fnum = 1;
        let target_freq = 200.0;
        let ampl = 1.0;
        let maxdepth = 2;
        let accuracy = 0.5;

        // Create an RFrequency array with two elements whose sum equals the target frequency
        let found_frequency_objects = vec![
            RFrequency { frequency_number: 2, frequency: 150.0, amplitude: 1.0 },
            RFrequency { frequency_number: 3, frequency: 50.0, amplitude: 1.0 },
        ];

        // Call check_for_composition
        let composition = check_for_composition(fnum, target_freq, ampl, maxdepth, accuracy, &found_frequency_objects);

        // Assert
        assert!(composition.composition_string.contains("f1=1f2+1f3"));
    }


    #[test]
    fn test_three_component_composition() {
        // Setup
        let fnum = 1;
        let target_freq = 300.0;
        let ampl = 1.0;
        let maxdepth = 3;
        let accuracy = 0.5;

        // Create an RFrequency array with three elements whose combination equals the target frequency
        let found_frequency_objects = vec![
            RFrequency { frequency_number: 2, frequency: 100.0, amplitude: 1.0 },
            RFrequency { frequency_number: 3, frequency: 100.0, amplitude: 1.0 },
            RFrequency { frequency_number: 4, frequency: 100.0, amplitude: 1.0 },
        ];

        // Call check_for_composition
        let composition = check_for_composition(fnum, target_freq, ampl, maxdepth, accuracy, &found_frequency_objects);

        // Assert
        assert!(composition.composition_string.contains("f1=1f2+1f3+1f4"));
    }


    #[test]
    fn test_selecting_simplest_composition() {
        // Setup
        let fnum = 1;
        let target_freq = 100.0;
        let ampl = 1.0;
        let maxdepth = 2;
        let accuracy = 0.5;

        // Create an RFrequency array with multiple possible compositions
        let found_frequency_objects = vec![
            RFrequency { frequency_number: 2, frequency: 50.0, amplitude: 1.0 },
            RFrequency { frequency_number: 3, frequency: 50.0, amplitude: 1.0 },
            RFrequency { frequency_number: 4, frequency: 100.0, amplitude: 1.0 },
        ];

        // Call check_for_composition
        let composition = check_for_composition(fnum, target_freq, ampl, maxdepth, accuracy, &found_frequency_objects);

        // Assert that the simplest composition is chosen
        assert_eq!(composition.composition_string, "f1=1f4;f1=1f2+1f3;f1=1f3+1f2;f1=1f4;f1=2f2;f1=2f3");
    }


    #[test]
    fn test_empty_frequency_array() {
        // Setup
        let fnum = 1;
        let target_freq = 100.0;
        let ampl = 1.0;
        let maxdepth = 1;
        let accuracy = 0.5;

        // Create an empty RFrequency array
        let found_frequency_objects = vec![];

        // Call check_for_composition
        let composition = check_for_composition(fnum, target_freq, ampl, maxdepth, accuracy, &found_frequency_objects);

        // Assert no compositions are found
        assert!(composition.composition_string.is_empty());
    }

}
